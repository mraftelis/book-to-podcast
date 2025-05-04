from gtts import gTTS
import os

def text_to_speech(text: str, language: str = 'en', save_path: str = "app/tests/summary_audio.mp3") -> str:
    """
    Convert text to speech using Google TTS and save as MP3.
    Returns the path to the generated file.
    """
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    tts = gTTS(text=text, lang=language)
    tts.save(save_path)
    print(f"Saving MP3 to: {save_path}")
    return save_path