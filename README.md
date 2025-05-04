# 📚 Book-to-Podcast Pipeline

This project takes a `.pdf` or `.mobi` book, summarizes it using OpenAI's GPT-4o, and converts the summary to audio (MP3) using Google TTS — turning books into short podcast episodes.

---

## 🚀 Features

- ✅ Upload `.pdf` or `.mobi` files
- ✅ Extract full text
- ✅ Summarize via GPT-4o with a target duration (e.g. 20–60 mins)
- ✅ Convert summary to speech using `gTTS`
- ✅ Save podcast-ready `.mp3` files

---

## 🔧 Setup

1. **Clone the repo**
2. **Create a `.env` file**
```env
OPENAI_API_KEY=your-openai-key# book-to-podcast

Install requirements
pip install -r requirements.txt

Run the pipeline
python3 -m app.pipeline


