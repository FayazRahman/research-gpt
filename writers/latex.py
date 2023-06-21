from .base import Writer

import loopgpt

LATEX_START = (
r"""\documentclass{book}

\title{<TITLE>}
\date{<DATE>}

\begin{document}

\maketitle

\tableofcontents
"""
)

class LatexWriter(Writer):
    @staticmethod
    @loopgpt.aifunc()
    def write_section(section: str) -> str:
        """This is a semantic function. Writes the introduction for the given section in LaTeX format.
        Do not use \section command, as this will be done automatically.

        Args:
            section (str): The section to write the introduction for.
        
        Returns:
            str: The introduction written in LaTeX format.
        """
        return r"\section\n\n" + section + "\n\n"
    
    @staticmethod
    @loopgpt.aifunc()
    def write_subsection(subsection: str) -> str:
        """This is a semantic function. Writes a short subsection about the given topic in LaTeX format.
        Includes links to relevant websites at the end of the subsection.
        Do not use \subsection command, as this will be done automatically.

        Args:
            subsection (str): The subsection to write about.
        
        Returns:
            str: The section written in LaTeX format.
        """
        return r"\subsection\n\n" + subsection + "\n\n"


class ShortLatexWriter(LatexWriter):
    @staticmethod
    @loopgpt.aifunc()
    def write_subsection(subsection: str) -> str:
        """This is a semantic function. Writes a short subsection about the given topic in LaTeX format.
        Includes links to relevant websites at the end of the subsection.

        Args:
            subsection (str): The subsection to write about.
        
        Returns:
            str: The section written in LaTeX format.
        """
        return r"\subsection\n\n" + subsection + "\n\n"
