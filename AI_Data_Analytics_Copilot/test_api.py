import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api = os.getenv("GEMINI_API_KEY")

print(api[:10])

genai.configure(api_key=api)

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content("Hello")

print(response.text)