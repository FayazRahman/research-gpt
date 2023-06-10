topic = input("Enter input text: ")

from typing import List
from collections import defaultdict
import openai
import os
import time

# openai.api_type = "azure"
# openai.api_base = "https://loopgpt-azure-openai.openai.azure.com/"
# openai.api_version = "2023-03-15-preview"
# openai.api_key = os.getenv("AZURE_OPENAI_KEY")

from loopgpt.models import AzureOpenAIModel, OpenAIModel
from loopgpt.embeddings import AzureOpenAIEmbeddingProvider, OpenAIEmbeddingProvider

# model = AzureOpenAIModel("loop-gpt-35-turbo")
# emb = AzureOpenAIEmbeddingProvider("loop-text-embedding-ada-002")
model = OpenAIModel()
emb = OpenAIEmbeddingProvider()

from utils import get_keywords_and_questions, research, clean_up, generate_section_and_paragraph_headings, generate_index, write_content, write_section_intro, get_subtopics
from loopgpt.tools import GoogleSearch, Browser 
from loopgpt.aifunc import create_empty_agent
from functools import partial
import loopgpt

research_agent = create_empty_agent(model=model, embedding_provider=emb)
writer_agent = create_empty_agent(model=model, embedding_provider=emb)

agent_kwargs = {
    "model": model,
    "embedding_provider": emb,
}

get_keywords_and_questions = partial(get_keywords_and_questions, agent_kwargs=agent_kwargs)
get_subtopics = partial(get_subtopics, agent=research_agent, agent_kwargs=agent_kwargs)
clean_up = partial(clean_up, agent_kwargs=agent_kwargs)
research = partial(research, agent=research_agent, agent_kwargs=agent_kwargs)
generate_section_and_paragraph_headings = partial(generate_section_and_paragraph_headings, agent_kwargs=agent_kwargs)
generate_index = partial(generate_index, agent=research_agent, agent_kwargs=agent_kwargs)
write_section_intro = partial(write_section_intro, agent=writer_agent, agent_kwargs=agent_kwargs)
write_content = partial(write_content, agent=writer_agent, agent_kwargs=agent_kwargs)

keywords_and_questions = get_keywords_and_questions(topic)[:1]
print(keywords_and_questions)

google_search = GoogleSearch()
browser = Browser()

google_search.agent = research_agent
browser.agent = research_agent

data_sources = {}

keywords_map = defaultdict(list)
depth = 1
i = 0
keywords_map[i] = keywords_and_questions[:]
while depth > 0:
    new_keywords = []
    while keywords_and_questions:
        search_term = keywords_and_questions.pop(0)
        _, links = google_search.manual_run(search_term)
        for j in range(2):
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

print(keywords_map)

heading_map = ""

def print_section(depth, section, lst):
    global heading_map
    heading_map += f"{'    ' * depth}{lst[section]}\n"
    if keywords_map[depth + 1]:
        for subsection in range(len(keywords_map[depth + 1][section])):
            print_section(depth + 1, subsection, keywords_map[depth + 1][section])

for section in range(len(keywords_map[0])):
    print_section(0, section, keywords_map[0])

print(heading_map)

heading_map = clean_up(heading_map)

print(heading_map)

index = generate_index(heading_map)

print(index)

items = index.split("\n")

txt = open("wwdc_2023.txt", "w")

current_heading = ""

writer_agent.memory = research_agent.memory

for item in items:
    n, heading = item.strip().split(" ", 1)
    if len(n) == 2:
        with writer_agent.query(heading):
            content = f"\n{heading}\n{'=' * len(heading)}\n\n{write_section_intro(heading)}\n"
        current_heading = heading
    else:
        with writer_agent.query(current_heading + ": " + heading):
            content = f"\n{heading}\n{'-' * len(heading)}\n\n{write_content(heading)}\n"
    print(content)
    txt.write(content)
