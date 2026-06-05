"""
Conditionals Quick Revision
"""

# Basic If Else

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")

# Multiple Conditions

marks = 82

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("Fail")

# Nested If

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login Successful")

# Ternary Operator

num = 17

result = "Even" if num % 2 == 0 else "Odd"

print(result)

# Chained Comparison

x = 15

print(10 < x < 20)           # Range Check

# Membership

language = "Python"

if "Py" in language:
    print("Found")

# all() and any()

print(all([True, True]))     # All True
print(any([0, 0, 1]))        # At Least One True

# Match Case

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid")