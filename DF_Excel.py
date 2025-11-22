import pandas as pd

def convert_to_dataframe(parsed_entries):
    df = pd.DataFrame(parsed_entries, columns=["Key", "Value", "Comments"])
    return df

def save_excel(df, path="output/Output.xlsx"):
    df.to_excel(path, index=False)