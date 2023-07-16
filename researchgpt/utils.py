from typing import List

from loopgpt.tools import GoogleSearch, Browser
import loopgpt


@loopgpt.aifunc()
def get_keywords(topic: str) -> List[str]:
    """This is an atomic function. This function helps the user learn about the given topic in detail.
    It returns a short list of 10 keywords that will be optimal for searching the web.

    Args:
        topic (str): The topic to get keywords for.

    Returns:
        List[str]: A list of 10 keywords about the topic.
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
def generate_outline(entities: List[str], title: str) -> str:
    """This is a semantic function. Creates an outline for an article about the given title that includes the given entities.

    Examples:
        1. Section 1
            1.1. Subsection 1
            1.2. Subsection 2
        2. Section 2
            3.1. Subsection 1

    Args:
        entities (List[str]): The entities to be included in the outline.
        title (str): The title of the document.

    Returns:
        str: The generated outline.
    """
