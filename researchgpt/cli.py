import os
import loopgpt
import argparse
import subprocess as sp

from .main import research, write_book
from .modes import get_research_args
from .config import model, emb


def main():
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
    parser.add_argument("--load", help="Load an agent from its state for reuse.")

    args = parser.parse_args()

    topic = args.topic
    filename = args.filename
    mode = args.mode
    agent_path = args.load

    if args.latex:
        mode = "latex-" + mode

    if agent_path:
        research_agent = loopgpt.Agent.load(agent_path)
    else:
        research_agent = loopgpt.empty_agent(model=model, embedding_provider=emb)

    writer_agent = loopgpt.empty_agent(model=model, embedding_provider=emb)

    writer_agent.memory = research_agent.memory

    research_args = get_research_args(mode)
    if args.breadth:
        research_args["breadth"] = int(args.breadth)
    if args.depth:
        research_args["depth"] = int(args.depth)

    dirname, _ = os.path.split(filename)

    try:
        if len(research_agent.memory) == 0:
            index = research(topic, research_agent, **research_args)
        else:
            index = research_agent.memory.get("index", k=1)[0]
            print(f"Index found in memory: \n\n{index}\n")

        write_book(topic, index, writer_agent, filename, mode)
        print(f"Content written to {filename}\n")

        if mode.startswith("latex") and filename.endswith(".tex"):
            output_dir = str(os.path.join(dirname, "research_output"))
            try:
                print(f"Converting {filename} to PDF...\n")
                for _ in range(3):
                    sp.call(
                        ["pdflatex", filename, "-output-directory", output_dir],
                        stdout=sp.DEVNULL,
                    )
            except Exception as e:
                raise Exception(
                    "LaTeX to PDF conversion failed. Make sure you have a TeX distribution installed."
                ) from e
    finally:
        agent_path = str(os.path.join(dirname, "research_agent.json"))
        research_agent.save(agent_path)
