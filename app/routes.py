from flask import Blueprint, request, jsonify, current_app
from app.utils.text_extractor import extract_text_from_pdf
from app.utils.data_cleaner import clean_text
from app.models.gemini_fallback import gemini_fallback
from app.models.hf_diploma import extract_diplomas  # Now uses Gemini
from app.models.hf_skill import extract_skills

main_bp = Blueprint('main', __name__)

@main_bp.route('/upload', methods=['POST'])
def upload_resume():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        # Extract and clean text
        raw_text = extract_text_from_pdf(file)
        cleaned_text = clean_text(raw_text)

        # Extract diplomas via Gemini
        diplomas = extract_diplomas(cleaned_text)

        # Extract skills via Gemini fallback
        skills = []
        try:
            skills = extract_skills(cleaned_text)
        except Exception as e:
            logging.warning(f"Skill extraction failed, falling back to Gemini: {str(e)}")
            fallback_data = gemini_fallback(cleaned_text)
            skills = fallback_data.get("skills", [])

        # Save to MongoDB
        resume_id = current_app.db.cvs.insert_one({
            "diplomas": diplomas,
            "skills": skills
        }).inserted_id

        return jsonify({
            "resume_id": str(resume_id),
            "diplomas": diplomas,
            "skills": skills
        }), 200

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "Failed to process CV"}), 500