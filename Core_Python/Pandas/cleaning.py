"""
Data Cleaning
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name":["Piyush",None,"Rahul"],
    "Marks":[90,np.nan,80]
})

print(df.isnull())          # Null Check

print(df.isnull().sum())    # Null Count

print(df.dropna())          # Remove Nulls

print(df.fillna(0))         # Fill Number

print(df.fillna("Unknown")) # Fill Text