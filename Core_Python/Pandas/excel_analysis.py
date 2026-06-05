import pandas as pd

df = pd.read_excel("students.xlsx")

print(df.head())            # First Rows

print(df.columns)           # Columns

print(df.shape)             # Shape

print(df.describe())        # Statistics

print(df.isnull().sum())    # Missing Values