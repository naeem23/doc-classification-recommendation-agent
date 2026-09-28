from pypdf import PdfReader
from core.parsing.base import Parser

class PdfParser(Parser):
    def extract_text(self, path: str) -> str:
        reader = PdfReader(path)
        return "\n".join(page.extract_text() or "" for page in reader.pages)