from app.utils.prompts import DIPLOMA_PROMPT, SKILL_PROMPT
from app.utils.gemini_utils import generate_and_parse
import logging


def gemini_fallback(text: str) -> dict:
    """Fallback extraction using Google Gemini with centralized prompts"""

    def parse_diplomas(response_text):
        """Parse diplomas from the Gemini response."""
        return [
            line.strip().lstrip("- ")  # Clean bullet points
            for line in response_text.split("\n")
            if line.strip() and "Formation" not in line  # Skip headers
        ]

    def parse_skills(response_text):
        """Parse skills from the Gemini response."""
        return [skill.strip() for skill in response_text.split(",") if skill.strip()]

    # Extract diplomas
    diplomas = generate_and_parse(DIPLOMA_PROMPT, text, parse_diplomas)

    # Extract skills
    skills = generate_and_parse(SKILL_PROMPT, text, parse_skills)

    return {"diplomas": diplomas, "skills": skills}