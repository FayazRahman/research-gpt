from writers import *


def get_research_args(mode):
    if mode.endswith("short"):
        return {"breadth": 4, "depth": 1}
    else:
        return {"breadth": 4, "depth": 2}


def get_writer(mode):
    if mode == "long":
        return TextWriter
    elif mode == "short":
        return ShortTextWriter
    elif mode == "latex-long":
        return LatexWriter
    elif mode == "latex-short":
        return ShortLatexWriter
    else:
        raise ValueError("Invalid mode.")
