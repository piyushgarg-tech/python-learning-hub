"""
Filtering Data
"""

import pandas as pd

df = pd.DataFrame({
    "Name":["Piyush","Rahul","Arun"],
    "Marks":[90,80,95],
    "Age":[20,21,19]
})

print(df[df["Marks"] > 85])      # Filter

print(df[df["Age"] >= 20])       # Condition

print(df.loc[:,["Name","Marks"]])# Select Cols

print(df.iloc[0])                # First Row

print(df.sort_values("Marks"))

print(df.sort_values(
    "Marks",
    ascending=False
))