import PyPDF2
import pytesseract
from PIL import Image
from io import BytesIO

def extract_text_from_pdf(file):
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        if not text.strip():
            image = Image.open(file)
            text = pytesseract.image_to_string(image)

        return text.strip()
    except Exception as e:
        raise ValueError(f"Text extraction failed: {str(e)}")