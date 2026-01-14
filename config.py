import os
from dotenv import load_dotenv

load_dotenv()

WEB_SEARCH_TOKEN = os.getenv("OLLAMA_API_KEY")
OR_TOKEN = os.getenv("OR_TOKEN")
MODEL = os.getenv("MODEL") or "mistralai/mistral-small-3.1-24b-instruct:free"

INFERENCE_BASE_URL = "https://openrouter.ai/api/v1"
