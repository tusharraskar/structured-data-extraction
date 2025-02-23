from llama_cloud_services import LlamaParse
from dotenv import load_dotenv
import os
import json
import nest_asyncio
import instructor
import google.generativeai as genai
from parsing_models import FullFinancialData

load_dotenv()
nest_asyncio.apply()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") 

class FinancialDocumentProcessor:
    def __init__(self, model_name: str = "models/gemini-2.0-flash", google_api_key: str = os.getenv("GOOGLE_API_KEY")):
        self.client = self.configure_genai(model_name, google_api_key)
    
    def parse_pdf(self,file_path) -> str:
        """
        Parses the PDF file and returns its content as a markdown string.
        """
        try:
            documents = LlamaParse(
                result_type="markdown",
                premium_mode=True,
                preserve_layout_alignment_across_pages=True,
                output_tables_as_HTML=True,
            ).load_data(file_path)
            return "\n\n---\n\n".join(
                doc.text_resource.text for doc in documents if hasattr(doc, 'text_resource') and doc.text_resource
            )
            
        except Exception as e:
            raise RuntimeError(f"Error parsing PDF: {e}")
    
    def configure_genai(self, model_name: str, google_api_key: str):
        """
        Configures the GenAI client with the given model name and API key.
        """
        genai.configure(api_key=google_api_key)
        return instructor.from_gemini(
            client=genai.GenerativeModel(
                model_name=model_name,
            ),
            mode=instructor.Mode.GEMINI_JSON,
        )
    
    def extract_financial_data(self, data) -> "FullFinancialData":
        """
        Extracts structured financial data and provides insights based on financial performance.
        """
        prompt = f"""
        The extracted financial data is as follows:
        
        {data}

        Please verify the accuracy of this data and provide insights based on financial performance.
        """
        
        response = self.client.messages.create(
            messages=[{"role": "user", "content": prompt}],
            response_model=FullFinancialData,
        )
        return response
    
    def save_financial_data_to_json(self, data, json_file_path):
        """
        Saves extracted financial data to a JSON file with the same name as the input PDF.
        """
        try:
            with open(json_file_path, "w", encoding="utf-8") as json_file:
                json.dump(data.dict(by_alias=True), json_file, indent=4)
            print(f"Financial data successfully saved to {json_file_path}")
        except Exception as e:
            raise RuntimeError(f"Error saving JSON file: {e}")

