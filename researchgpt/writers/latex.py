from .base import Writer

import loopgpt

LATEX_TEMPLATE = """\\documentclass{{report}}

\\title{{{title}}}
\\date{{{date}}}
\\author{{Research-GPT}}

\\begin{{document}}

\\maketitle

\\tableofcontents

{content}

\\end{{document}}
"""

LATEX_CONTEXT = r"""
Always enhance your writing with the following instructions:

To underline text, use the \underline{} command.

To emphasize text, use the \emph{} command.

To write math, use the $ symbol to enclose math expressions. For example, $x^2 + y^2 = z^2$.

To escape special characters, use the backslash (\) symbol before the character you want to escape. For example, if you want to write a percent sign (%) in your document, you should write \%.

To create a bulleted list in LaTeX, one can use the itemize environment, where each element starts with the \item command.

For URLs, use the \url{} command.

\begin{itemize}
  \item First item
  \item Second item
  \item Third item
\end{itemize}

"""


class LatexWriter(Writer):
    @staticmethod
    @loopgpt.aifunc()
    def write_section(section: str) -> str:
        """Writes a latex \section{} command with the section name and then a short section about the given topic in less than 50 words.

        Args:
            section (str): The section to write about.

        Returns:
            str: The introduction written in LaTeX format.
        """

    @staticmethod
    @loopgpt.aifunc()
    def write_subsection(subsection: str) -> str:
        """Writes a latex \subsection{} command with the subsection name and then a detailed subsection about the given topic that should contain as much
        details as possible including reference links. The subsection should be between 500 and 1000 words long and should cover the topic in depth.

        Args:
            subsection (str): The subsection to write about.

        Returns:
            str: The section written in LaTeX format.
        """


class ShortLatexWriter(LatexWriter):
    @staticmethod
    @loopgpt.aifunc()
    def write_subsection(subsection: str) -> str:
        """Writes a latex \subsection{} command with the subsection name and then a short subsection about the given topic that should be between 100 and 200
        words long. Includes any relevant links that were found previously where the reader can find more information.

        Args:
            subsection (str): The subsection to write about.

        Returns:
            str: The section written in LaTeX format.
        """
