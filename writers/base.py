import loopgpt

from abc import ABC, abstractmethod

# abstract_static_aifunc = lambda x: abstractmethod(staticmethod(loopgpt.aifunc()(x)))

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
