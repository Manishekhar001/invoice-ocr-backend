from openpyxl import Workbook
import uuid, os

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_excel_file(data: dict) -> str:
    wb = Workbook()
    ws = wb.active
    ws.append(["Invoice No", "Date", "Total"])
    ws.append([data.get("invoice_no"), data.get("date"), data.get("total")])
    fname = f"invoice_{uuid.uuid4().hex[:6]}.xlsx"
    path = os.path.join(OUTPUT_DIR, fname)
    wb.save(path)
    return path
