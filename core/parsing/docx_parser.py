import docx
from core.parsing.base import Parser

class DocxParser(Parser):
    def extract_text(self, path: str) -> str:
        doc = docx.Document(path)
        return "\n".join(p.text for p in doc.paragraphs)