from abc import ABC, abstractmethod

class Parser(ABC):
    @abstractmethod
    def extract_text(self, path: str) -> str:
        pass 

    