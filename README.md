# 📄 PDF → Structured Excel Extraction System

This project converts an unstructured PDF into a clean, machine-readable Excel sheet using a custom parsing logic based entirely on rule-based text extraction.

It identifies key fields such as:

- Personal Information  
- Education  
- Work Experience  
- Certifications  
- Skill Ratings  
- Misc. contextual lines  

and converts them into a structured tabular format.

A Streamlit interface allows users to upload a PDF, view extracted data, and download the final Excel output.

---

## 🚀 Features

| Feature | Description |
|--------|------------|
| 📥 PDF Upload | Upload any input document through the Streamlit UI |
| 🧠 Smart Parsing | Extracts meaningful fields using rule-based regex logic |
| 🏷 Field Categorization | Identifies Name, DOB, Education, Skills, etc. |
| 📊 Live Preview | Displays parsed content in a clean table format |
| 📤 Export to Excel | Download processed data as `Output.xlsx` |
| 🌐 Deployable | Configured to run on Vercel using FastAPI + Streamlit bridge |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| UI | Streamlit |
| Parsing / Processing | Python, Regex |
| PDF Text Extraction | pdfplumber |
| File Output | Pandas + openpyxl |
| Deployment | Vercel, FastAPI, Uvicorn |

---
#install dependencies:
pip install -r requirements.txt

#Run the UI:
streamlit run streamlit_UI.py


## 📁 Project Structure

