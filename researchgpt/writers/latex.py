from .base import Writer

import loopgpt

LATEX_TEMPLATE = """\\documentclass{{report}}

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
        """Writes a latex \section{} command with the section name and then a short section about the given topic without going into specific details 
        as there will be future subsections for that. The section should be less than 50 words long and should mention at least 3 subtopics 
        that will be covered in future subsections.

        Args:
            section (str): The section to write the introduction for.

        Returns:
            str: The introduction written in LaTeX format.
        """

    @staticmethod
    @loopgpt.aifunc()
    def write_subsection(subsection: str) -> str:
        """Writes a latex \subsection{} command with the subsection name and then a detailed subsection about the given topic that should contain as much 
        details as possible including reference links. The subsection should be between 500 and 1000 words long and should cover the topic in depth. 
        It must be in valid LaTeX with correct escaping.

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
        Writes a latex \subsection{} command with the subsection name and then a short subsection about the given topic that should be between 100 and 200 
        words long. It must be in valid LaTeX with correct escaping. Includes any relevant links that were found previously where the reader can 
        find more information.

        Args:
            subsection (str): The subsection to write about.

        Returns:
            str: The section written in LaTeX format.
        """
