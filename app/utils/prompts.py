# app/utils/prompts.py

# Diploma Extraction Prompt
DIPLOMA_PROMPT = """
Extract academic qualifications (degrees, diplomas, and institutions) from the 'Education' or 'Formation' section of this CV.
Include only recognized diplomas such as Baccalauréat, Bachelor, Licence, Master, PhD, or Doctorat.
Include the degree name, institution, and dates. Exclude certifications, courses, or training programs.
Return the diplomas as a clean list with one entry per line.
Examples:
- 2022-2025: Bachelor of Science in Computer Science, University of XYZ
- 2020-2022: Master of Business Administration, ABC Institute
- 2018-2019: Baccalauréat, Sciences Techniques, Lycée El Mourouj 4

CV Text:
{text}
"""

# Skill Extraction Prompt
SKILL_PROMPT = """
Extract technical skills, programming languages, frameworks, methodologies, and domain-specific expertise from this CV.
Exclude tools, software names, or platforms (e.g., Git, Docker, Jira). Focus on competencies that demonstrate expertise.
Return the skills as a clean, comma-separated list without additional formatting or headers.
Examples:   
Java, Python, JavaScript, ReactJS, Django, Agile, Scrum, Web Development, IoT

CV Text:
{text}
"""