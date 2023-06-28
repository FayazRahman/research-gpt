from typing import List

from loopgpt.tools import GoogleSearch, Browser
import loopgpt


@loopgpt.aifunc()
def get_keywords_and_questions(topic: str) -> List[str]:
    """This is an atomic function. This function helps the user learn about the given topic in detail.
    It returns a short list of 10 keywords and questions that will be optimal for searching the web.

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
def clean_up(index: str) -> str:
    """This is an atomic function. Remove duplicate sections and subsections from the given index.

    Args:
        index (str): Index to clean up.

    Returns:
        str: The cleaned up index.
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
def generate_index(topics: List[str], title: str) -> str:
    """This is a semantic function. The given topics were researched by the user. He would now like to write a book with the given title.
    This function helps the user by generating an index for the book based on the topics researched.

    Examples:
        1. Section 1
            1.1. Subsection 1
            1.2. Subsection 2
        2. Section 2
            3.1. Subsection 1

    Args:
        topics (List[str]): The topics researched by the user.
        title (str): The title of the book.

    Returns:
        str: The generated index.
    """
