from collections import defaultdict, OrderedDict

from .utils import (
    get_keywords_and_questions,
    generate_index,
)
from loopgpt.tools import GoogleSearch, Browser
from loopgpt.agent import Agent
from .modes import get_writer, get_template
from datetime import date

import os


def research(topic: str, research_agent: Agent, breadth: int = 3, depth: int = 1):
    keywords_and_questions = get_keywords_and_questions(topic)[:breadth]

    google_search = GoogleSearch()
    browser = Browser()

    data_sources = {}
    topics_researched = []

    with research_agent:
        while depth > 0:
            new_keywords = []
            while keywords_and_questions:
                search_term = keywords_and_questions.pop(0)
                topics_researched.append(search_term)
                print(f"Searching Google for: {topic} {search_term}\n")
                _, links = google_search.manual_run(topic + " " + search_term)
                for j in range(breadth):
                    if data_sources.get(links[j]):
                        pass
                    else:
                        print(f"Browsing: {links[j]}\n")
                        data_sources[links[j]] = browser.run(links[j], "")

                with research_agent.query(search_term):
                    subtopics = get_keywords_and_questions(search_term)[:breadth]
                    new_keywords.extend(subtopics[:])

            keywords_and_questions = new_keywords[:]
            depth -= 1

    index = generate_index(topics_researched, topic)
    research_agent.memory.add(index, "index")
    print(f"Index generated:\n\n{index}\n")

    return index


def write_book(topic, index, writer_agent, filename, mode):
    items = index.split("\n")

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    file = open(filename, "w", encoding="utf-8")

    current_heading = ""

    writer = get_writer(mode)
    template = get_template(mode)

    content = ""
    last_section = ""
    with writer_agent:
        for item in items:
            n, heading = item.strip().split(" ", 1)
            if len(n) == 2:
                with writer_agent.query(topic + ": " + heading):
                    print(f"Writing section: {heading}\n")
                    last_section = writer.write_section(topic, heading)
                    content += last_section + "\n\n"
                current_heading = heading
            else:
                with writer_agent.complete({"assistant": last_section}):
                    with writer_agent.query(
                        topic + ": " + current_heading + ": " + heading
                    ):
                        print(f"Writing subsection: {heading}\n")
                        content += writer.write_subsection(topic, heading) + "\n\n"
    file.write(template.format(title=topic, date=str(date.today()), content=content))
    file.close()
