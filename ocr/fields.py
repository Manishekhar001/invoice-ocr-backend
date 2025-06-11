import re

def extract_invoice_fields(text: str) -> dict:
    return {
        "invoice_no": find(r"Invoice\s*(No|Number)[:\-]?\s*(\w+)", text, 2),
        "date": find(r"Date[:\-]?\s*([0-9]{2}/[0-9]{2}/[0-9]{4})", text),
        "total": find(r"Total[:\-]?\s* ₹?([\d,]+\.?\d*)", text)
    }

def find(pattern, text, group=1):
    m = re.search(pattern, text, re.IGNORECASE)
    return m.group(group) if m else None
