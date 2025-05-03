import os
import pytest
from app.summarizer import summarize_text
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.skipif(
    not os.getenv("OPENAI_API_KEY"),
    reason="OPENAI_API_KEY not set in environment"
)
def test_summarize_text():
    sample_text = (
        "Artificial intelligence (AI) refers to the simulation of human intelligence in machines "
        "that are programmed to think and learn. These machines can perform tasks that typically "
        "require human intelligence, such as visual perception, speech recognition, decision-making, "
        "and language translation."
    )
    summary = summarize_text(sample_text, target_duration_minutes=1)
    assert isinstance(summary, str)
    assert len(summary) > 0
