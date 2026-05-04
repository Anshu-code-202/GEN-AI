# test_gemini.py

import os
from dotenv import load_dotenv
import google.generativeai as genai  # temporary; migrate to google.genai later

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

# Correct model
model = genai.GenerativeModel("gemini-2.0-flash",temperature=0.9)

response = model.generate_content(
    "Explain AI in one line"
)

print(response.text)
