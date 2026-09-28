from core.parsing.base import Parser

class TextParser(Parser):
    def extract_text(self, path: str) -> str:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()