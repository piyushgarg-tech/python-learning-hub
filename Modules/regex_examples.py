"""
Regex Quick Revision
"""

import re

text = "My phone is 9876543210"

# Search

match = re.search(r"\d+", text)

print(match.group())           # First Number

# Find All

print(
    re.findall(r"\d", text)
)                              # All Digits

# Replace

print(
    re.sub(r"\d", "*", text)
)                              # Hide Digits

# Email Validation

email = "test@gmail.com"

pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

print(
    bool(
        re.match(pattern, email)
    )
)