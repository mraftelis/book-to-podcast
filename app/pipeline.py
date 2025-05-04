from app.extractor import extract_text_from_pdf
from app.summarizer import summarize_text
from app.tts import text_to_speech
import os

def run_full_pipeline(pdf_path: str, output_mp3_path: str = "output/summary.mp3"):
    print(f"🚀 Starting full pipeline for: {pdf_path}")

    # Step 1: Extract text from PDF
    print("📄 Extracting text...")
    full_text = extract_text_from_pdf(pdf_path)

    if not full_text or len(full_text.strip()) == 0:
        print("❌ No text extracted. Aborting.")
        return

    # Step 2: Summarize text
    print("🧠 Summarizing text...")
    summary = summarize_text(full_text, target_duration_minutes=20)

    # Step 3: Convert summary to speech
    print("🔊 Converting to audio...")
    mp3_path = text_to_speech(summary, save_path=output_mp3_path)

    print(f"✅ Pipeline complete! Audio saved to: {mp3_path}")

if __name__ == "__main__":
    run_full_pipeline("app/tests/sample.pdf", output_mp3_path="output/summary.mp3")