import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("VT_API_KEY")
BASE_URL = "https://www.virustotal.com/api/v3"

if not API_KEY:
    raise ValueError("API key not found. Set VT_API_KEY in .env")