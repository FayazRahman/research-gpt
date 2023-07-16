from .utils import (
    get_keywords,
    generate_outline,
)
from loopgpt.tools import GoogleSearch, Browser
from loopgpt.agent import Agent
from .modes import get_writer, get_template, get_context
from datetime import date

import os


def research(topic: str, research_agent: Agent, breadth: int = 3, depth: int = 1):
    keywords = get_keywords(topic, [])[:breadth]

    google_search = GoogleSearch()
    browser = Browser()

    data_sources = {}
    topics_researched = []
    topics_researched.extend(keywords)

    with research_agent:
        while depth > 0:
            new_keywords = []
            while keywords:
                search_term = keywords.pop(0)
                print(f"Searching Google for: {topic} {search_term}\n")
                _, links = google_search(topic + " " + search_term)
                for j in range(breadth):
                    if data_sources.get(links[j]):
                        pass
                    else:
                        print(f"Browsing: {links[j]}\n")
                        data_sources[links[j]] = browser(links[j])

                with research_agent.query(search_term):
                    subtopics = get_keywords(search_term, topics_researched)[:breadth]
                    topics_researched.extend(subtopics)
                    new_keywords.extend(subtopics)

            keywords = new_keywords[:]
            depth -= 1

    index = generate_outline(topics_researched, topic)
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
    context = get_context(mode)

    content = ""
    last_section = ""

    with writer_agent:
        for item in items:
            try:
                n, heading = item.strip().split(" ", 1)
            except ValueError:
                continue
            if len(n) == 2:
                with writer_agent.query(topic + ": " + heading):
                    print(f"Writing section: {heading}\n")
                    last_section = writer.write_section(heading)
                    content += last_section + "\n\n"
                current_heading = heading
            else:
                with writer_agent.complete(
                    {"assistant": last_section, "system": context}
                ):
                    with writer_agent.query(
                        topic + ": " + current_heading + ": " + heading
                    ):
                        print(f"Writing subsection: {heading}\n")
                        content += writer.write_subsection(heading) + "\n\n"
    file.write(template.format(title=topic, date=str(date.today()), content=content))
    file.close()
