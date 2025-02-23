# Financial Data Extraction: Documentation

## Introduction

This document provides an overview of the tools used, steps to run the solution, and challenges faced in extracting financial data from PDFs. The solution involves parsing PDF documents, extracting structured financial data, and saving it in a JSON format.

## Tools Used

### 1. LlamaParse

- Used for **PDF parsing** and extracting text with layout preservation.
- Supports **premium mode** for better table extraction.
- Converts tables into **HTML format** to maintain structure.

### 2. Google Gemini AI (via Generative AI API)

- Used for **extracting financial data** from parsed text.
- Model: `gemini-2.0-flash`.
- Provides structured responses using the `instructor` library.

### 3. Instructor

- Enables structured output from LLM responses.
- Used to format the extracted financial data as per `FullFinancialData` schema.

### 4. Nest Asyncio

- Allows running **asynchronous tasks** inside Jupyter and scripts.

### 5. Streamlit

- Provides a **UI for file uploads and downloads**.
- Displays the extracted financial data in **JSON format**.

### 6. Python Standard Libraries

- `os` : Handles file operations.
- `json` : Saves and displays extracted data in JSON format.
- `dotenv` : Loads environment variables.

## Steps to Run the Solution

### 1. Setup Environment

- Install dependencies:

  ```sh
  pip install -r requirements.txt
  ```

- Set up **Google API Key** and **Llama Cloud API Key** in a `.env` file:

  ```sh
  GOOGLE_API_KEY=your_google_api_key_here
  LLAMA_CLOUD_API_KEY=your_llama_api_key_here
  ```

  **Note:** Currently, free API keys are being used, which have usage limitations.

### 2. Run the Streamlit App

```sh
streamlit run streamlit_ui.py
```

### 3. Upload a PDF File

- Select a **financial report PDF** from your local system.
- Click the **"Start Processing"** button.

### 4. Processing Stages

1. **Parsing PDF**: Extracts text and tables using `LlamaParse`.
2. **Extracting Financial Data**: Uses `Google Gemini AI` to structure the extracted information.
3. **Displaying Output**: Shows extracted financial data and provides a **JSON download** option.

### 5. Download Extracted Data

- Click the **"Download JSON Output"** button.
- The file will have the **same name as the uploaded PDF** but with a `.json` extension.

## Challenges Faced

### 1. Parsing PDF Content

- PDFs contain **unstructured text, tables, and images**.
- Some PDFs have **scanned images** making text extraction difficult.

  **Solution:** Used `LlamaParse` with **premium mode** and `preserve_layout_alignment_across_pages` to improve accuracy.

### 2. Maintaining Table Structure

- Extracted tables often **lose their format** when converted to text.

  **Solution:** Used `output_tables_as_HTML=True` to preserve the structure.

- Post-processing is done to **convert HTML tables into structured JSON** for financial data representation.

## Known Issues

- The solution does not work well on `data (20).pdf`.

## Conclusion

This solution efficiently extracts financial data from PDFs while handling text and table parsing challenges. Using `LlamaParse` for structured extraction and `Google Gemini AI` for financial insights ensures accuracy and usability. 
