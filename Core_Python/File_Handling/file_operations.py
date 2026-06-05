"""
File Handling Quick Revision
"""

from pathlib import Path

# Write

with open("sample.txt", "w") as f:
    f.write("Hello Python\n")

# Read

with open("sample.txt") as f:
    print(f.read())

# Append

with open("sample.txt", "a") as f:
    f.write("New Line\n")

# Read Line By Line

with open("sample.txt") as f:
    for line in f:
        print(line.strip())

# Readlines

with open("sample.txt") as f:
    lines = f.readlines()

print(lines)

# Pathlib

file = Path("sample.txt")

print(file.exists())          # Exists

if file.exists():
    print(file.stat().st_size) # Size

# Copy File

with open("sample.txt") as src, open("copy.txt", "w") as dst:
    dst.write(src.read())

# Word Count

with open("sample.txt") as f:
    print(len(f.read().split()))