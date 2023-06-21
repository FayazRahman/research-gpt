from collections import defaultdict

from utils import (
    get_keywords_and_questions,
    clean_up,
    generate_index,
    get_subtopics,
)
from loopgpt.tools import GoogleSearch, Browser
from modes import get_writer

def research(topic, research_agent, breadth=3, depth=1):
    keywords_and_questions = get_keywords_and_questions(topic)[:breadth]
    print(keywords_and_questions)

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
                    next_level = get_subtopics(search_term)[:4]

                print(next_level)
                keywords_map[i + 1].append(next_level[:])
                new_keywords.extend(next_level)
            keywords_and_questions = new_keywords[:]
            depth -= 1
            i += 1

    heading_map = ""

    def print_section(depth, section, lst):
        nonlocal heading_map
        heading_map += f"{'    ' * depth}{lst[section]}\n"
        if keywords_map[depth + 1]:
            for subsection in range(len(keywords_map[depth + 1][section])):
                print_section(depth + 1, subsection, keywords_map[depth + 1][section])


    for section in range(len(keywords_map[0])):
        print_section(0, section, keywords_map[0])
    
    heading_map = clean_up(heading_map)
    index = generate_index(heading_map)
    print(index)
    
    return index

def write_book(index, writer_agent, filename, mode):
    items = index.split("\n")

    file = open(filename, "w")

    current_heading = ""

    writer = get_writer(mode)
    with writer_agent:
        for item in items:
            n, heading = item.strip().split(" ", 1)
            if len(n) == 2:
                with writer_agent.query(heading):
                    content = f"\n{heading}\n{'=' * len(heading)}\n\n{writer.write_section(heading)}\n"
                current_heading = heading
            else:
                with writer_agent.query(current_heading + ": " + heading):
                    content = (
                        f"\n{heading}\n{'-' * len(heading)}\n\n{writer.write_subsection(heading)}\n"
                    )
            print(content)
            file.write(content)
    file.close()
