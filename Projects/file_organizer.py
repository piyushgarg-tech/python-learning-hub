"""
File Organizer
"""

from pathlib import Path

downloads = Path("Downloads")

for file in downloads.iterdir():

    if file.is_file():

        ext = file.suffix[1:] or "others"

        target = downloads / ext

        target.mkdir(exist_ok=True)

        file.rename(target / file.name)