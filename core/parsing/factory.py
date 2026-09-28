import os
from core.parsing.text_parser import TextParser
from core.parsing.docx_parser import DocxParser
from core.parsing.pdf_parser import PdfParser

_PARSERS = {
    ".txt": TextParser(),
    ".docx": DocxParser(),
    ".pdf": PdfParser(),
}

def get_parser(path: str):
    ext = os.path.splitext(path)[1].lower()
    parser = _PARSERS.get(ext)
    if parser is None:
        raise ValueError(f"Unsupported file type: {ext}")
    return parser

