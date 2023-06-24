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
def generate_index(bad_index: str) -> str:
    """This is a semantic function. Given is an index for a book, but it has many problems, for example, duplicate sections, 
    bad section names, subsections that don't match their sections, missing numbering or sections without subsections. 
    This function fixes all of these problems and returns a properly numbered good index without duplicate sections or missing subsections.

    Examples:
        1. Section 1
            1.1. Subsection 1
            1.2. Subsection 2
        2. Section 2
            3.1. Subsection 1
    
    Args:
        bad_index (str): The bad index to be fixed.

    Returns:
        str: The generated good index.
    """
