"""
DataFrame Basics
"""

import pandas as pd

df = pd.DataFrame({
    "Name":["Piyush","Rahul","Arun"],
    "Marks":[90,80,95],
    "Age":[20,21,19]
})

print(df)

print(df.head())            # First Rows

print(df.tail())            # Last Rows

print(df.info())            # Structure

print(df.describe())        # Statistics

print(df.shape)             # Rows, Cols

print(df.columns)           # Column Names