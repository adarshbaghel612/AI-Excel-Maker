import streamlit as st
import pandas as pd
from parsing import parse_semantic_blocks
import pdfplumber
from io import BytesIO

st.title("PDF → Parsed Entries (Notebook Logic Only)")
st.write("This UI uses ONLY notebook code, with no additions or changes.")

uploaded = st.file_uploader("Upload PDF File", type=["pdf"])

if uploaded:

    # Extract text
    with pdfplumber.open(uploaded) as pdf:
        text = "\n".join(
            page.extract_text() for page in pdf.pages if page.extract_text()
        )

    # Parse using notebook logic
    entries = parse_semantic_blocks(text)

    # Convert entries directly to DataFrame (NO build_expected_output)
    df_output = pd.DataFrame(entries, columns=["Key", "Value", "Comments"])

    # Show table
    st.dataframe(df_output)

    # Download Excel
    excel_buffer = BytesIO()
    df_output.to_excel(excel_buffer, index=False)

    st.download_button(
        "Download Output.xlsx",
        data=excel_buffer.getvalue(),
        file_name="Output.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )