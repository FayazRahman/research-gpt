from .base import Writer, format

import loopgpt

TEXT_TEMPLATE = """{title}

{date}

{content}
"""


class TextWriter(Writer):
    @staticmethod
    @format(
        lambda heading, content: f"\n{heading}\n{'=' * len(heading)}\n\n{content}"
    )
    @loopgpt.aifunc()
    def write_section(section: str) -> str:
        """This is a semantic function. Write an short introduction for a section of a book that will be read by a general audience in an
        engaging and informative tone.

        Args:
            section (str): The section to write an introduction for.

        Returns:
            str: The introduction written.
        """

    @staticmethod
    @format(
        lambda heading, content: f"\n{heading}\n{'-' * len(heading)}\n\n{content}"
    )
    @loopgpt.aifunc()
    def write_subsection(subsection: str) -> str:
        """This is a semantic function. Only based on the data loaded into your memory, write content for a subsection of a book that will be read by
        a general audience in an engaging and informative tone. Stick to the subsection, as the reader has already been introduced to the general topic.
        Include as many details as possible.

        Args:
            subsection (str): The subsection to write about.

        Returns:
            str: The content written.
        """


class ShortTextWriter(TextWriter):
    @staticmethod
    @loopgpt.aifunc()
    @format(
        lambda heading, content: f"\n{heading}\n{'-' * len(heading)}\n\n{content}"
    )
    def write_subsection(subsection: str) -> str:
        """This is a semantic function. Write a short paragraph about the given subsection. Mention URLs that can be visited for further information.

        Args:
            subsection (str): The subsection to write a short description for.

        Returns:
            str: The written content.
        """
