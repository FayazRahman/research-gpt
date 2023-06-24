from .base import Writer

import loopgpt

LATEX_TEMPLATE = """\\documentclass{{book}}

\\title{{{title}}}
\\date{{{date}}}

\\begin{{document}}

\\maketitle

\\tableofcontents

{content}

\\end{{document}}
"""


class LatexWriter(Writer):
    @staticmethod
    @loopgpt.aifunc()
    def write_section(section: str) -> str:
        """This is a semantic function. It writes a latex section command followed by the section name and then an introduction for the section.

        Args:
            section (str): The section to write the introduction for.

        Returns:
            str: The introduction written in LaTeX format.
        """

    @staticmethod
    @loopgpt.aifunc()
    def write_subsection(subsection: str) -> str:
        """This is a semantic function. It writes a latex subsection command followed by the subsection name and then a very descriptive subsection content.

        Args:
            subsection (str): The subsection to write about.

        Returns:
            str: The section written in LaTeX format.
        """


class ShortLatexWriter(LatexWriter):
    @staticmethod
    @loopgpt.aifunc()
    def write_subsection(subsection: str) -> str:
        """This is a semantic function. It writes a latex subsection command followed by the subsection name and then a very short subsection
        content including links to relevant websites.

        Args:
            subsection (str): The subsection to write about.

        Returns:
            str: The section written in LaTeX format.
        """
