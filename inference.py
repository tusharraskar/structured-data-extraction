import os
import json
from helper import FinancialDocumentProcessor

pdf_file_path = "data (13).pdf"  # Change this to your file path

if not os.path.exists(pdf_file_path):
    raise FileNotFoundError(f"File not found: {pdf_file_path}")

processor = FinancialDocumentProcessor()

try:
    print("📄 Parsing PDF...")
    parsed_text = processor.parse_pdf(pdf_file_path)
    print("✅ PDF Parsing Completed!")

    print("🔍 Extracting Financial Data...")
    extracted_data = processor.extract_financial_data(parsed_text)
    print("✅ Data Extraction Completed!")

    processor.save_financial_data_to_json(extracted_data, "output.json")

    extracted_json = json.dumps(extracted_data.dict(by_alias=True), indent=4)
    print("\n📊 Extracted Financial Data:\n", extracted_json)

except Exception as e:
    print(f"❌ Error: {e}")
