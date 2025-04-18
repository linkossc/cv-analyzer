import google.generativeai as genai
from app.config import Config
from app.utils.prompts import DIPLOMA_PROMPT, SKILL_PROMPT
import logging

genai.configure(api_key=Config.GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-latest')

def gemini_fallback(text: str) -> dict:
    """Fallback extraction using Google Gemini with centralized prompts"""
    try:
        # Extract diplomas
        diploma_response = model.generate_content(DIPLOMA_PROMPT.format(text=text))
        diplomas = [
            line.strip().lstrip("- ")  # Clean bullet points
            for line in diploma_response.text.split("\n")
            if line.strip() and "Formation" not in line  # Skip headers
        ]

        # Extract skills
        skill_response = model.generate_content(SKILL_PROMPT.format(text=text))
        skills = [skill.strip() for skill in skill_response.text.split(",") if skill.strip()]

        return {"diplomas": diplomas, "skills": skills}

    except Exception as e:
        logging.error(f"Gemini fallback error: {str(e)}")
        return {"diplomas": [], "skills": []}