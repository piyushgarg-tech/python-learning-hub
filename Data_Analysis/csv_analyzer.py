"""
CSV Analyzer
"""

import pandas as pd

df = pd.read_csv("data.csv")

print(df.shape)            # Rows & Cols

print(df.columns)          # Columns

print(df.describe())       # Statistics

print(df.isnull().sum())   # Missing Values