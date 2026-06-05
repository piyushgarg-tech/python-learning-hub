"""
GroupBy and Merge Examples
"""

import pandas as pd

students = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Class": [10, 10, 11],
    "Marks": [90, 80, 95]
})

fees = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Fee": [5000, 6000, 5500]
})

# GroupBy

print(
    students.groupby(
        "Class"
    )["Marks"].mean()
)

# Merge

print(
    pd.merge(
        students,
        fees,
        on="Name"
    )
)