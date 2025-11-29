#!/usr/bin/python3
"""
1-write_file module
defines a ftion that writes a UTF-8 string to a text file
and ret the number of characters written.
"""


def write_file(filename="", text=""):
    """
    text file and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
