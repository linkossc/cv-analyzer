import google.generativeai as genai
from app.config import Config
import logging

# Configure Gemini API
genai.configure(api_key=Config.GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-latest')


def generate_and_parse(prompt_template, text, parse_func):
    """
    Generate content using Gemini and parse the response using the provided parse function.

    Args:
        prompt_template (str): The prompt template to format with the text.
        text (str): The input text to process.
        parse_func (callable): A function to parse the response text.

    Returns:
        list: Parsed results from the Gemini response.
    """
    try:
        # Generate content using Gemini
        response = model.generate_content(prompt_template.format(text=text))

        # Parse the response using the provided parse function
        return parse_func(response.text)
    except Exception as e:
        logging.error(f"Gemini processing error: {str(e)}")
        return []