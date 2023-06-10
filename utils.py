from typing import List

from loopgpt.tools import GoogleSearch, Browser
import loopgpt


@loopgpt.aifunc()
def get_keywords_and_questions(topic: str) -> List[str]:
    """This is an atomic function. This function helps the user learn about the given topic in detail.
    It returns a list of keywords and questions that will be optimal for searching the web.

    Args:
        topic (str): The topic to get keywords and questions for.

    Returns:
        List[str]: A list of keywords and questions about the topic.
    """

@loopgpt.aifunc(tools=[GoogleSearch, Browser])
def research(topic: str) -> List[str]:
    """This function searches the topic on Google and browses the first link. It returns a list of the most important sub-topics 
    (in order of decreasing importance) obtained from the browsed pages that can be explored further.

    Args:
        topic (str): The topic to research.

    Returns:
        List[str]: A list of important sub-topics learned
    """

@loopgpt.aifunc()
def get_subtopics(topic: str) -> List[str]:
    """This is an atomic function. It returns a list of sub-topics for the given topic that will be worth exploring further.

    Args:
        topic (str): The topic to get sub-topics for.

    Returns:
        List[str]: A list of sub-topics for the given topic.
    """

@loopgpt.aifunc()
def clean_up(keywords: str) -> str:
    """This is an atomic function. It takes a list of keywords and cleans it up by removing similar keywords.

    Args:
        keywords str: The list of keywords to clean up.

    Returns:
        str: The cleaned up keywords in same order.
    """

@loopgpt.aifunc()
def generate_section_and_paragraph_headings(context: str) -> List[str]:
    """This is an atomic function. It takes a context and generates a list of short and concise headings.

    Args:
        context (str): The context to generate headings for.

    Returns:
        List[str]: The list of headings generated.
    """

@loopgpt.aifunc()
def generate_index(clues: List[str]) -> str:
    """This is a semantic function. It generates a numbered index for a short book using the given clues.
    There should be never be two sections about the same topic. Section names should be short and distinct and they cannot be questions. 
    Every section should have at least one subsection.

    Examples:
        1. Section 1
            1.1. Subsection 1
            1.2. Subsection 2
        2. Section 2
            3.1. Subsection 1

    Args:
        clues (List[str]): The clues to generate the index from.
    
    Returns:
        str: The generated index.
    """

@loopgpt.aifunc()
def write_section_intro(section: str) -> str:
    """This is a semantic function. Write an short introduction for a section of a book that will be read by a general audience in an 
    engaging and informative tone.

    Args:
        section (str): The section to write an introduction for.
    
    Returns:
        str: The introduction written.
    """

@loopgpt.aifunc()
def write_content(subsection: str) -> str:
    """This is a semantic function. Only based on the data loaded into your memory, write content for a subsection of a book that will be read by 
    a general audience in an engaging and informative tone. Remember to write specifically about the subsection since the reader is already 
    familiar with the topic.

    Args:
        subsection (str): The subsection to write about.
    
    Returns:
        str: The content written.
    """
