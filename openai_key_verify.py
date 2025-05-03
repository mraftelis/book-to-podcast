from dotenv import load_dotenv
import os
import openai

# Load the .env file
load_dotenv()

# Get the API key
api_key = os.getenv("OPENAI_API_KEY")

# Check if key is loaded
if not api_key:
    print("❌ OPENAI_API_KEY not found in .env file.")
    exit(1)

openai.api_key = api_key

# Attempt to list models
try:
    response = openai.models.list()
    print("✅ OpenAI API key is working. Models available:")
    for model in response.data[:5]:  # Show just the first 5
        print("  -", model.id)
except openai.error.AuthenticationError:
    print("❌ Invalid OpenAI API key.")
except Exception as e:
    print(f"❌ Other error: {e}")