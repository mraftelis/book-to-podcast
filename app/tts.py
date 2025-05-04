from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def text_to_speech(text: str, save_path: str = "output/summary.mp3") -> str:
    """
    Convert text to speech using OpenAI TTS (HD model) and save as MP3.
    Returns the path to the generated file.
    """
    response = client.audio.speech.create(
        model="tts-1-hd",
        voice="nova",
        input=text
    )

    # Ensure output directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, "wb") as f:
        f.write(response.content)

    print(f"✅ MP3 saved to: {save_path}")
    return save_path