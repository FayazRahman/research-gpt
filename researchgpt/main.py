from collections import defaultdict, OrderedDict

from utils import (
    get_keywords_and_questions,
    generate_index,
)
from loopgpt.tools import GoogleSearch, Browser
from modes import get_writer, get_template
from datetime import date


def research(topic, research_agent, breadth=3, depth=1):
    keywords_and_questions = get_keywords_and_questions(topic)[:breadth]

    google_search = GoogleSearch()
    browser = Browser()

    data_sources = {}
    keywords_map = defaultdict(list)

    i = 0
    keywords_map[i] = keywords_and_questions[:]
    with research_agent:
        while depth > 0:
            new_keywords = []
            while keywords_and_questions:
                search_term = keywords_and_questions.pop(0)
                _, links = google_search.manual_run(topic + " " + search_term)
                for j in range(breadth):
                    if data_sources.get(links[j]):
                        pass
                    else:
                        data_sources[links[j]] = browser.run(links[j], "")

                with research_agent.query(search_term):
                    subtopics = get_keywords_and_questions(search_term)
                    next_level = subtopics[:4]
                    next_keywords = subtopics[:breadth]

                keywords_map[i + 1].append(next_level[:])
                new_keywords.extend(next_keywords[:])
            keywords_and_questions = new_keywords[:]
            depth -= 1
            i += 1

    keywords_map.pop(i)

    heading_map = ""

    def print_section(depth, section, lst):
        nonlocal heading_map
        heading_map += f"{'    ' * depth}{lst[section]}\n"
        if keywords_map[depth + 1]:
            for subsection in range(len(keywords_map[depth + 1][section])):
                print_section(depth + 1, subsection, keywords_map[depth + 1][section])

    for section in range(len(keywords_map[0])):
        print_section(0, section, keywords_map[0])

    index = generate_index(heading_map)

    return index


def write_book(topic, index, writer_agent, filename, mode):
    items = index.split("\n")

    file = open(filename, "w")

    current_heading = ""

    writer = get_writer(mode)
    template = get_template(mode)

    content = ""
    last_section = ""
    with writer_agent:
        for item in items:
            n, heading = item.strip().split(" ", 1)
            if len(n) == 2:
                with writer_agent.query(heading):
                    last_section = writer.write_section(heading)
                    content += last_section + "\n\n"
                current_heading = heading
            else:
                with writer_agent.complete({"assistant": last_section}):
                    with writer_agent.query(current_heading + ": " + heading):
                        content += writer.write_subsection(heading) + "\n\n"
    file.write(template.format(title=topic, date=str(date.today()), content=content))
    file.close()
