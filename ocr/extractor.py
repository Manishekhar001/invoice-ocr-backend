from pdf2image import convert_from_bytes
import pytesseract
from PIL import Image
import io

def ocr_from_pdf(pdf_bytes: bytes) -> str:
    images = convert_from_bytes(pdf_bytes)
    full_text = ""
    for i, img in enumerate(images):
        text = pytesseract.image_to_string(img)
        full_text += f"\n--- Page {i+1} ---\n" + text
    return full_text
