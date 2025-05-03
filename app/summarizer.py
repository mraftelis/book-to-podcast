from dotenv import load_dotenv
import os
from openai import OpenAI
from typing import List

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = "gpt-4o"

def chunk_text(text: str, max_tokens: int = 3000) -> List[str]:
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        current_chunk.append(word)
        current_length += 1
        if current_length >= max_tokens:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_length = 0

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

def summarize_text(text: str, target_duration_minutes: int = 20) -> str:
    chunks = chunk_text(text)
    summaries = []

    for chunk in chunks:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": f"Please summarize the following text:\n\n{chunk}"}
            ],
            temperature=0.5,
            max_tokens=1000
        )
        summary = response.choices[0].message.content.strip()
        summaries.append(summary)

    return ' '.join(summaries)