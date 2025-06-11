from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from ocr.extractor import ocr_from_pdf
from ocr.fields import extract_invoice_fields
from excel.generator import generate_excel_file

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your Lovable domain if needed
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-invoice")
async def upload_invoice(file: UploadFile = File(...)):
    contents = await file.read()
    raw_text = ocr_from_pdf(contents)
    fields = extract_invoice_fields(raw_text)
    excel_path = generate_excel_file(fields)
    return {
        "fields": fields,
        "excel_path": excel_path
    }
