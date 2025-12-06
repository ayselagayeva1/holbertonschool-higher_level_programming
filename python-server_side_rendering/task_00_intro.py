#!/usr/bin/python3
"""
Simple Templating Program
"""

import os

def generate_invitations(template, attendees):
    # --- Check input types ---
    if not isinstance(template, str):
        print(f"Error: template must be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: attendees must be a list of dictionaries, got {type(attendees).__name__}")
        return

    # --- Handle empty inputs ---
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # --- Process each attendee ---
    for idx, attendee in enumerate(attendees, start=1):
        output = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output = output.replace(f"{{{key}}}", str(value))

        # --- Write to output file ---
        filename = f"output_{idx}.txt"
        try:
            with open(filename, "w") as f:
                f.write(output)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
