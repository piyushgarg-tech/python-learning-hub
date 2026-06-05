"""
Strings Quick Revision
"""

s = "Piyush Garg"

# Indexing

print(s[0])                      # First Character
print(s[-1])                     # Last Character

# Slicing

print(s[:6])                     # Start -> 5
print(s[7:])                     # 7 -> End
print(s[::-1])                   # Reverse

# Case Conversion

print(s.upper())                 # Uppercase
print(s.lower())                 # Lowercase
print(s.title())                 # Title Case
print(s.swapcase())              # Swap Case

# Search

print(s.find("Garg"))            # Index
print("Piyush" in s)             # Membership

# Replace

print(
    s.replace("Garg", "Sharma")
)                                # Replace Text

# Count

print("banana".count("a"))       # Count Occurrences

# Start / End

print(s.startswith("P"))         # Starts With
print(s.endswith("g"))           # Ends With

# Remove Spaces

text = "   hello world   "

print(text.strip())              # Both Sides
print(text.lstrip())             # Left Side
print(text.rstrip())             # Right Side

# Split & Join

data = "python,java,c++"

langs = data.split(",")

print(langs)

print("-".join(langs))           # Join

# Comparisons

print("apple" < "banana")
print("abc" == "ABC")

# f-string

name = "Piyush"
marks = 95

print(f"{name} scored {marks}")

# Validation

print("123".isdigit())           # Digits
print("hello".isalpha())         # Alphabets
print("hello123".isalnum())      # Alpha Numeric

# Formatting

print("{:<10}".format("Python")) # Left Align
print("{:^10}".format("Python")) # Center Align
print("{:>10}".format("Python")) # Right Align