#!/usr/bin/python3
"""6-load_from_json_file module"""

import json


def load_from_json_file(filename):
    """Create an object from a JSON file."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
