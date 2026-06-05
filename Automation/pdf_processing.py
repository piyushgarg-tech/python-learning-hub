"""
PDF Processing
"""

from pypdf import PdfReader

reader = PdfReader("sample.pdf")

print(len(reader.pages))      # Total Pages

print(
    reader.pages[0].extract_text()
)                             # First Page Text