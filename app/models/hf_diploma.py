from app.utils.prompts import DIPLOMA_PROMPT
from app.utils.gemini_utils import generate_and_parse
import logging


def extract_diplomas(text):
    """Extract diplomas using Gemini."""

    def parse_diplomas(response_text):
        """Parse diplomas from the Gemini response."""
        diplomas = []
        for line in response_text.split("\n"):
            if line.strip() and "Formation" not in line:  # Skip headers
                # Clean bullet points
                line = line.strip().lstrip("- ")

                # Extract date range and diploma details
                parts = line.split(":")
                if len(parts) < 2:
                    continue  # Skip malformed lines

                date_range, diploma_details = parts[0].strip(), ":".join(parts[1:]).strip()

                # Parse start and end years
                years = date_range.split("-")
                if len(years) != 2:
                    continue  # Skip invalid date ranges

                start_year, end_year = years[0].strip(), years[1].strip()

                # Determine graduation year
                if end_year.isdigit():  # Valid graduation year
                    diplomas.append(f"{end_year}: {diploma_details}")
                elif end_year.lower() == "present":  # Still studying
                    logging.info(f"Excluding ongoing study: {line}")

        return diplomas

    return generate_and_parse(DIPLOMA_PROMPT, text, parse_diplomas)