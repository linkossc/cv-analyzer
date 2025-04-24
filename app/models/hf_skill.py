from app.utils.prompts import SKILL_PROMPT
from app.utils.gemini_utils import generate_and_parse
import logging


def extract_skills(text):
    """Extract skills using Gemini."""

    def parse_skills(response_text):
        """Parse skills from the Gemini response."""
        return [skill.strip() for skill in response_text.split(",") if skill.strip()]

    return generate_and_parse(SKILL_PROMPT, text, parse_skills)