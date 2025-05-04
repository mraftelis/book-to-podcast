from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
import tempfile

from app.extractor import extract_text_from_pdf
from app.summarizer import summarize_text
from app.tts import text_to_speech

app = FastAPI()

""" # Serve static HTML
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def read_root():
    return FileResponse("app/static/index.html") """

@app.post("/generate-podcast")
async def generate_podcast(file: UploadFile = File(...)):
    suffix = os.path.splitext(file.filename)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    # Extract → Summarize → Convert to audio
    text = extract_text_from_pdf(tmp_path)
    summary = summarize_text(text, target_duration_minutes=20)
    output_path = "output/summary.mp3"
    mp3_path = text_to_speech(summary, save_path=output_path)
    print("EXTRACTED TEXT (first 500 chars):")
    print(text[:500])

    print("\nSUMMARY (first 500 chars):")
    print(summary[:500])    

    return FileResponse(mp3_path, media_type="audio/mpeg", filename="summary.mp3")