"""
File Renaming
"""

from pathlib import Path

folder = Path("files")

for i, file in enumerate(folder.iterdir(), start=1):
    file.rename(
        folder / f"file_{i}{file.suffix}"
    )

print("Done")