import os
from pdf_reader import extract_pdf_text
from parsing import parse_semantic_blocks
from DF_Excel import convert_to_dataframe
from DF_Excel import save_excel

pdf_text = extract_pdf_text("/content/Data Input.pdf")
entries = parse_semantic_blocks(pdf_text)
df = convert_to_dataframe(entries)


os.makedirs('output', exist_ok=True)

save_excel(df)
print("Output.xlsx generated successfully!")