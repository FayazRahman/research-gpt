from .base import Writer, format

import loopgpt

TEXT_TEMPLATE = """{title}

{date}

{content}
"""


class TextWriter(Writer):
    @staticmethod
    @format(lambda heading, content: f"\n{heading}\n{'=' * len(heading)}\n\n{content}")
    @loopgpt.aifunc()
    def write_section(section: str) -> str:
        """Writes a short section about the given topic without going into specific details as there will be future subsections for that.
        The section should be less than 50 words long and should mention at least 3 subtopics that will be covered in future subsections.

        Args:
            section (str): The topic of the section.

        Returns:
            str: The section content.
        """

    @staticmethod
    @format(lambda heading, content: f"\n{heading}\n{'-' * len(heading)}\n\n{content}")
    @loopgpt.aifunc()
    def write_subsection(subsection: str) -> str:
        """Writes a detailed subsection about the given topic that should contain as much details as possible including reference links.
        The subsection should be between 500 and 1000 words long and should cover the topic in depth. Please include at least 1 reference link
        from a reputable source.

        Args:
            subsection (str): The topic of the subsection.

        Returns:
            str: The subsection content.
        """


class ShortTextWriter(TextWriter):
    @staticmethod
    @loopgpt.aifunc()
    @format(lambda heading, content: f"\n{heading}\n{'-' * len(heading)}\n\n{content}")
    def write_subsection(subsection: str) -> str:
        """Writes a short subsection about the given topic that should be between 100 and 200 words long. Inlcudes any relevant links that were found
        previously where the reader can find more information.

        Args:
            subsection (str): The topic of the subsection.

        Returns:
            str: The subsection content.
        """
