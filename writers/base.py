import loopgpt

from abc import ABC, abstractmethod
from functools import wraps
from typing import Callable


class Writer(ABC):
    @staticmethod
    @abstractmethod
    @loopgpt.aifunc()
    def write_section(section: str) -> str:
        ...

    @staticmethod
    @abstractmethod
    @loopgpt.aifunc()
    def write_subsection(subsection: str) -> str:
        ...


class format:
    def __init__(self, format: Callable):
        self.format = format

    def __call__(self, func):
        @wraps(func)
        def inner(*args, **kwargs):
            response = func(*args, **kwargs)
            return self.format(*args, response, **kwargs)

        return inner
