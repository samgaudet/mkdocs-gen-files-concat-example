"""
This script concatenates the file contents from ./release_notes.
Each file is read and its content is added to the "Release notes" page.
Within each page, the header is converted from h1 (#) to h2 (##).
"""
import os
from typing import List

import mkdocs_gen_files

RELEASE_NOTES_FILE = "release-notes.md"
RELEASE_NOTES_FOLDER = "release_notes"

releases: List[str] = ["# Release notes\n"]

for file in os.listdir(RELEASE_NOTES_FOLDER):
    with open(f"{RELEASE_NOTES_FOLDER}/{file}", "r") as release_note:
        release = release_note.read()
        releases.append(release.replace("# ", "## "))

with mkdocs_gen_files.open(RELEASE_NOTES_FILE, "w") as release_notes:
    release_notes.write("\n".join(releases))
