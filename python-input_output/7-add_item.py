#!/usr/bin/python3
"""Add all arguments to a Python list, and save them to a file"""

import sys
from pathlib import Path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

FILENAME = "add_item.json"

# Load existing list if file exists, else start with empty list
items = []
if Path(FILENAME).is_file():
    items = load_from_json_file(FILENAME)

# Add all command-line arguments (excluding the script name)
items.extend(sys.argv[1:])

# Save updated list back to file
save_to_json_file(items, FILENAME)
