from fastapi import FastAPI, UploadFile, File, HTTPException
from app.extractor import extract_text_from_pdf, convert_mobi_to_text
import tempfile
import os

app = FastAPI()

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    suffix = os.path.splitext(file.filename)[1].lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        if suffix == ".pdf":
            text = extract_text_from_pdf(tmp_path)
        elif suffix == ".mobi":
            text = convert_mobi_to_text(tmp_path)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type.")
    finally:
        os.remove(tmp_path)

    return {"text": text[:1000]}  # Only return first 1000 chars for testing
