#!/usr/bin/python3
"""
0-read_file module
This module defines a function that reads a UTF-8 text file and prints its content to stdout.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
