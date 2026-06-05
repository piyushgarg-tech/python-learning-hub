"""
Office Automation Examples

Concepts Covered:
- Excel Processing
- Report Generation
- School Fee Analysis
"""

import pandas as pd


# =====================================
# Excel Automation
# =====================================

df = pd.read_excel("students.xlsx")

print(df.head())

df["Total"] = df["Math"] + df["Science"]

df.to_excel(
    "result.xlsx",
    index=False
)


# =====================================
# Report Generation
# =====================================

report_df = pd.DataFrame({
    "Name": ["Piyush", "Rahul"],
    "Marks": [90, 80]
})

report = report_df.describe()

report.to_csv("report.csv")

print(report)


# =====================================
# School Work Automation
# =====================================

fees_df = pd.read_excel("fees.xlsx")

total_fee = fees_df["Fee"].sum()

pending = fees_df[
    fees_df["Status"] == "Pending"
]

print(total_fee)

print(len(pending))

pending.to_excel(
    "pending_students.xlsx",
    index=False
)