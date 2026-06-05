"""
Data Analysis Examples

Concepts Covered:
- Attendance Analysis
- Expense Analysis
- Student Analysis
- Practice Projects
"""

import pandas as pd


# =====================================
# Attendance Analysis
# =====================================

attendance = pd.read_excel(
    "attendance.xlsx"
)

print(
    attendance["Present"].mean() * 100
)


# =====================================
# Expense Analysis
# =====================================

expenses = pd.read_excel(
    "expenses.xlsx"
)

print(
    expenses["Amount"].sum()
)

print(
    expenses.groupby(
        "Category"
    )["Amount"].sum()
)


# =====================================
# Student Analysis
# =====================================

students = pd.read_csv(
    "students.csv"
)

print(
    students["Marks"].mean()
)

print(
    students["Class"].value_counts()
)


# =====================================
# Practice Project
# =====================================

sales = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar"],
    "Sales": [1000, 1500, 1200]
})

print(
    sales["Sales"].sum()
)

print(
    sales["Sales"].mean()
)