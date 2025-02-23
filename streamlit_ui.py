# import streamlit as st
# import json
# import os
# from helper import FinancialDocumentProcessor


# st.title("Financial Data Extraction")

# uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

# if uploaded_file is not None:
#     file_path = os.path.join("user_data", uploaded_file.name)

#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())

#     processor = FinancialDocumentProcessor(file_path)

#     with st.status("📄 Parsing PDF... Please wait", expanded=True) as pdf_status:
#         markdown_content = processor.parse_pdf()
#         pdf_status.update(label="✅ PDF Parsing Completed!", state="complete")

#     with st.status("🔍 Extracting Data... Please wait", expanded=True) as extract_status:
#         extracted_data = processor.extract_financial_data(markdown_content)
#         extract_status.update(label="✅ Data Extraction Completed!", state="complete")

#     extracted_json = extracted_data.dict(by_alias=True)
#     json_string = json.dumps(extracted_json, indent=4)

#     st.subheader("📊 Extracted Data")
#     st.download_button(
#         label="📥 Download JSON Output",
#         data=json_string,
#         file_name="extracted_financial_data.json",
#         mime="application/json"
#     )
#     st.json(extracted_json)




# import streamlit as st
# import json
# import os
# from helper import FinancialDocumentProcessor

# st.title("Financial Data Extraction")

# if "extracted_data" not in st.session_state:
#     st.session_state.extracted_data = None
#     st.session_state.extracted_json = None
#     st.session_state.file_path = None

# uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

# if uploaded_file is not None and st.session_state.extracted_data is None:
#     os.makedirs("user_data", exist_ok=True)
#     file_path = os.path.join("user_data", uploaded_file.name)

#     try:
#         with open(file_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())

#         processor = FinancialDocumentProcessor(file_path)

#         with st.status("📄 Parsing PDF... Please wait", expanded=True) as pdf_status:
#             markdown_content = processor.parse_pdf()
#             pdf_status.update(label="✅ PDF Parsing Completed!", state="complete")

#         with st.status("🔍 Extracting Data... Please wait", expanded=True) as extract_status:
#             extracted_data = processor.extract_financial_data(markdown_content)
#             extract_status.update(label="✅ Data Extraction Completed!", state="complete")

#         st.session_state.extracted_data = extracted_data
#         st.session_state.extracted_json = json.dumps(extracted_data.dict(by_alias=True), indent=4)
#         st.session_state.file_path = file_path

#     except Exception as e:
#         st.error(f"❌ An error occurred: {e}")

#     finally:
#         if os.path.exists(file_path):
#             os.remove(file_path)

# if st.session_state.extracted_data is not None:
#     st.subheader("📊 Extracted Data")
#     st.download_button(
#         label="📥 Download JSON Output",
#         data=st.session_state.extracted_json,
#         file_name="extracted_data.json",
#         mime="application/json"
#     )
#     st.json(st.session_state.extracted_json)





import streamlit as st
import json
import os
from helper import FinancialDocumentProcessor

st.title("Financial Data Extraction")

if "extracted_data" not in st.session_state:
    st.session_state.extracted_data = None
    st.session_state.extracted_json = None
    st.session_state.file_path = None
    st.session_state.prev_uploaded_file = None  # Track previous file
    st.session_state.process_started = False  # Track if processing has started

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

# 🔹 Reset session state if a new file is uploaded
if uploaded_file is not None and uploaded_file.name != st.session_state.get("prev_uploaded_file"):
    st.session_state.extracted_data = None
    st.session_state.extracted_json = None
    st.session_state.file_path = None
    st.session_state.prev_uploaded_file = uploaded_file.name  # Track uploaded file
    st.session_state.process_started = False  # Reset process state

# 🔹 Show "Start Processing" button after file upload
if uploaded_file is not None and not st.session_state.process_started:
    if st.button("🚀 Start Processing"):
        st.session_state.process_started = True  # Mark process as started

if uploaded_file is not None and st.session_state.process_started and st.session_state.extracted_data is None:
    os.makedirs("user_data", exist_ok=True)
    file_path = os.path.join("user_data", uploaded_file.name)

    try:
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        processor = FinancialDocumentProcessor()

        with st.status("📄 Parsing PDF... Please wait", expanded=True) as pdf_status:
            markdown_content = processor.parse_pdf(file_path)
            pdf_status.update(label="✅ PDF Parsing Completed!", state="complete")

        with st.status("🔍 Extracting Data... Please wait", expanded=True) as extract_status:
            extracted_data = processor.extract_financial_data(markdown_content)
            extract_status.update(label="✅ Data Extraction Completed!", state="complete")

        st.session_state.extracted_data = extracted_data
        st.session_state.extracted_json = json.dumps(extracted_data.dict(by_alias=True), indent=4)
        st.session_state.file_path = file_path

    except Exception as e:
        st.error(f"❌ An error occurred: {e}")

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

if st.session_state.extracted_data is not None:
    st.subheader("📊 Extracted Data")
    base_filename = os.path.splitext(uploaded_file.name)[0]
    st.download_button(
        label="📥 Download JSON Output",
        data=st.session_state.extracted_json,
        file_name=f"{base_filename}.json",
        mime="application/json"
    )
    st.json(st.session_state.extracted_json)
