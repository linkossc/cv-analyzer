import google.generativeai as genai
from app.config import Config
from app.utils.prompts import DIPLOMA_PROMPT
import logging

genai.configure(api_key=Config.GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-latest')

def extract_diplomas(text):
    try:
        # Use centralized diploma prompt
        response = model.generate_content(DIPLOMA_PROMPT.format(text=text))
        diplomas = [
            line.strip().lstrip("- ")  # Clean bullet points
            for line in response.text.split("\n")
            if line.strip() and "Formation" not in line  # Skip headers
        ]
        return diplomas
    except Exception as e:
        logging.error(f"Diploma extraction error: {str(e)}")
        return []