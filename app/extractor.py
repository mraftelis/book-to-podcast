import fitz  # PyMuPDF
import subprocess
import os
import tempfile

def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def convert_mobi_to_text(file_path: str) -> str:
    with tempfile.TemporaryDirectory() as tmpdir:
        epub_path = os.path.join(tmpdir, "converted.epub")
        text_path = os.path.join(tmpdir, "converted.txt")
        subprocess.run(["ebook-convert", file_path, epub_path], check=True)
        subprocess.run(["ebook-convert", epub_path, text_path], check=True)
        with open(text_path, "r", encoding="utf-8") as f:
            return f.read()
