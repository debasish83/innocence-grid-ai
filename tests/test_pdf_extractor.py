import os
import tempfile
import PyPDF2
from src.pdf_gemini_parser.pdf_extractor import PDFExtractor

def make_pdf(path: str, text: str):
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    c = canvas.Canvas(path, pagesize=letter)
    c.drawString(72, 720, text)
    c.save()

def test_extract_text():
    extractor = PDFExtractor()
    with tempfile.TemporaryDirectory() as d:
        pdf_path = os.path.join(d, "sample.pdf")
        try:
            import reportlab  # ensure available
        except ImportError:
            return  # skip if reportlab not installed
        make_pdf(pdf_path, "Hello World")
        out = extractor.extract_text(pdf_path)
        assert "Hello" in out

def test_chunking():
    extractor = PDFExtractor()
    text = "Line\n" * 100
    chunks = extractor.chunk(text, 50)
    assert len(chunks) > 1
