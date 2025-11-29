#!/usr/bin/python3
"""
2-append_write module

Appendsto a text file and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appto a UTF-8 text file and returns the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
