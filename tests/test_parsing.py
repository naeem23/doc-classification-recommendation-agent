from core.parsing.factory import get_parser

def test_txt():
    text = get_parser("test_docs/sample.txt").extract_text("test_docs/sample.txt")
    assert len(text) > 0

def test_docx():
    text = get_parser("test_docs/sample.docx").extract_text("test_docs/sample.docx")
    assert len(text) > 0

def test_pdf():
    text = get_parser("test_docs/sample.pdf").extract_text("test_docs/sample.pdf")
    assert len(text) > 0