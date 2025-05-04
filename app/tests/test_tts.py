import os
from app.tts import text_to_speech

def test_text_to_speech_creates_file():
    sample_text = "This is a test of the emergency broadcast system. This is only a test."
    output_path = "app/tests/summary_audio.mp3"

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Generate audio
    generated_path = text_to_speech(sample_text, save_path=output_path)

    # Assertions
    assert os.path.exists(generated_path)
    assert generated_path.endswith(".mp3")
    print(f"✅ MP3 file created: {generated_path}")