"""
CSV Analysis
"""

import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())                # First Rows

print(df.info())                # Structure

print(df.describe())            # Statistics

print(
    df["column_name"]
    .value_counts()
)                               # Frequency

print(
    df.groupby("column_name")
    .size()
)                               # Group Count