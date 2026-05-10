import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

INPUT_FILE = "C:/Users/Adarsh/Downloads/Exported Items.bib"
OUTPUT_FILE = "cleaned.bib"

KEEP_FIELDS = {
    "inproceedings": {
        "author", "title", "booktitle", "pages",
        "year", "doi", "volume"
    },
    "article": {
        "author", "title", "journal", "volume",
        "number", "pages", "year", "doi"
    },
    "misc": {
        "author", "title", "year",
        "eprint", "archiveprefix",
        "primaryclass", "doi"
    }
}

def clean_entry(entry):
    entry_type = entry.get("ENTRYTYPE", "").lower()

    # Keep original ENTRYTYPE and ID exactly as-is
    cleaned = {
        "ENTRYTYPE": entry["ENTRYTYPE"],
        "ID": entry["ID"]
    }

    if entry_type in KEEP_FIELDS:
        allowed = KEEP_FIELDS[entry_type]

        for key, value in entry.items():
            if key.lower() in allowed:
                cleaned[key] = value

        # arXiv handling
        if entry_type == "misc":
            cleaned["archivePrefix"] = "arXiv"
            if "primaryclass" not in {k.lower() for k in entry}:
                cleaned["primaryClass"] = "cs.CV"

    else:
        for key in ["author", "title", "year", "doi"]:
            if key in entry:
                cleaned[key] = entry[key]

    return cleaned


# Load
with open(INPUT_FILE, encoding="utf-8") as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Clean
cleaned_entries = [clean_entry(entry) for entry in bib_database.entries]

# Write
new_db = BibDatabase()
new_db.entries = cleaned_entries

writer = BibTexWriter()
writer.indent = "  "
writer.order_entries_by = None

with open(OUTPUT_FILE, "w", encoding="utf-8") as bibfile:
    bibfile.write(writer.write(new_db))

print(f"Cleaned file written to {OUTPUT_FILE}")