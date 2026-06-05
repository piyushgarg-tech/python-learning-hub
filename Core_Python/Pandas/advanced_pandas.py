"""
Advanced Pandas
"""

import pandas as pd

students = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Class": [10, 10, 11],
    "Marks": [90, 80, 95]
})

# value_counts
print(students["Class"].value_counts())

# groupby
print(
    students.groupby("Class")["Marks"].mean()
)

# apply
print(
    students["Marks"].apply(
        lambda x: x + 5
    )
)

fees = pd.DataFrame({
    "Name": ["A", "B"],
    "Fee": [5000, 6000]
})

# merge
print(
    pd.merge(
        students,
        fees,
        on="Name",
        how="left"
    )
)

# pivot table
print(
    pd.pivot_table(
        students,
        values="Marks",
        index="Class"
    )
)