# MkDocs Gen Files Concatenation Example

This repository includes a minimal example for using [mkdocs-gen-files](https://oprypin.github.io/mkdocs-gen-files/) to concatenate release note files.
The specific implementation is highly subjective and the file structure, file naming, file content, and script are all _examples_.
When built, the files in `./release_notes` are concatenated and the _Release notes_ page renders as follows:

![release_notes_page](https://github.com/user-attachments/assets/3cec76fd-56b5-41db-b8ce-c9ab1a7d924f)

This example is an "MVP" and does not even use [_MkDocs Material_](https://squidfunk.github.io/mkdocs-material/) or anything more complex.

I hope it helps!

## Try it yourself!

Try messing around with and running the documentation yourself:

```bash
git clone git@github.com:samgaudet/mkdocs-gen-files-concat-example.git
cd mkdocs-gen-files-concat-example
python -m venv venv
venv/bin/activate
python -m pip install -r requirements.txt
python -m mkdocs serve
```
