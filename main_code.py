import pytesseract
from PIL import Image
import re
import pyairtable

# Airtable Configuration
AIRTABLE_API_KEY = "your_airtable_api_key"
BASE_ID = "your_base_id"
TABLE_NAME = "Receipts"
table = pyairtable.Table(AIRTABLE_API_KEY, BASE_ID, TABLE_NAME)

def extract_text(image: Image.Image) -> str:
    
    return pytesseract.image_to_string(image)

def extract_invoice_details(text: str) -> dict:
    
    details = {}
    invoice_number_match = re.search(r'Invoice\s*No\.?\s*(\S+)', text, re.IGNORECASE)
    details['Invoice Number'] = invoice_number_match.group(1) if invoice_number_match else 'N/A'
    
    date_match = re.search(r'(\d{2,4}[-/.]\d{1,2}[-/.]\d{1,2})', text)
    details['Date'] = date_match.group(1) if date_match else 'N/A'
    
    total_match = re.search(r'Total\s*[:$]?\s*(\d+[,.]\d{2})', text, re.IGNORECASE)
    details['Total Amount'] = total_match.group(1) if total_match else 'N/A'
    
    tax_match = re.search(r'Tax\s*[:$]?\s*(\d+[,.]\d{2})', text, re.IGNORECASE)
    details['Tax Amount'] = tax_match.group(1) if tax_match else 'N/A'
    
    return details

def save_to_airtable(details: dict):
    
    table.create(details)

def calculate_automatic_tax(base_amount: float, gst_rate: float, sale_type: str) -> dict:
    
    gst_amount = base_amount * gst_rate / 100
    total = base_amount + gst_amount
    if sale_type == "Intra-State":
        cgst = gst_amount / 2
        sgst = gst_amount / 2
        return {"CGST": cgst, "SGST": sgst, "Total Amount": total}
    else:
        return {"IGST": gst_amount, "Total Amount": total}
