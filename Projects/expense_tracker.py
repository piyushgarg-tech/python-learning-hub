"""
Expense Tracker
"""

expenses = []

while True:

    amount = float(
        input("Amount (0 to stop): ")
    )

    if amount == 0:
        break

    expenses.append(amount)

print(sum(expenses))      # Total

print(max(expenses))      # Highest

print(min(expenses))      # Lowest