from app.extractor import extract_text_from_pdf
import os

def test_pdf_extraction():
    sample_path = "app/tests/sample.pdf"
    assert os.path.exists(sample_path), "Missing sample PDF"
    text = extract_text_from_pdf(sample_path)
    assert isinstance(text, str)
    assert len(text) > 0
