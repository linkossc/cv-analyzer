import google.generativeai as genai
from app.config import Config
from app.utils.prompts import SKILL_PROMPT

genai.configure(api_key=Config.GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-latest')


def extract_skills(text):
    try:
        # Use centralized skill prompt
        response = model.generate_content(SKILL_PROMPT.format(text=text))

        # Parse the response into a clean list of skills
        skills = [skill.strip() for skill in response.text.split(",") if skill.strip()]
        return skills
    except Exception as e:
        logging.error(f"Skill extraction error: {str(e)}")
        return []