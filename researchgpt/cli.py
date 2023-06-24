import argparse
import subprocess as sp

from loopgpt.aifunc import create_empty_agent
from .main import research, write_book
from .modes import get_research_args
from .config import model, emb


def main():
    research_agent = create_empty_agent(model=model, embedding_provider=emb)
    writer_agent = create_empty_agent(model=model, embedding_provider=emb)

    parser = argparse.ArgumentParser()

    parser.add_argument("topic", help="Topic to research")
    parser.add_argument(
        "filename",
        help="Filename to write the research.",
    )
    parser.add_argument(
        "--mode",
        choices=["short", "long"],
        help="Mode of research.",
        default="short",
    )
    parser.add_argument(
        "--latex",
        help="Latex mode",
        action="store_true",
    )
    parser.add_argument(
        "--breadth",
        help="Breadth of research.",
    )
    parser.add_argument(
        "--depth",
        help="Depth of research.",
    )

    args = parser.parse_args()

    topic = args.topic
    filename = args.filename
    mode = args.mode

    if args.latex:
        mode = "latex-" + mode

    research_agent = create_empty_agent(model=model, embedding_provider=emb)
    writer_agent = create_empty_agent(model=model, embedding_provider=emb)

    writer_agent.memory = research_agent.memory

    research_args = get_research_args(mode)
    if args.breadth:
        research_args["breadth"] = int(args.breadth)
    if args.depth:
        research_args["depth"] = int(args.depth)

    index = research(topic, research_agent, **research_args)
    write_book(topic, index, writer_agent, filename, mode)
    print(f"Content written to {filename}\n")

    if mode.startswith("latex") and filename.endswith(".tex"):
        try:
            print(f"Converting {filename} to PDF...\n")
            for _ in range(3):
                sp.call(
                    ["pdflatex", filename, "-output-directory", f"./research_output/"],
                    stdout=sp.DEVNULL,
                )
        except Exception as e:
            raise Exception(
                "LaTeX to PDF conversion failed. Make sure you have a TeX distribution installed."
            ) from e
