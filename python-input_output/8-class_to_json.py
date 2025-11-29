#!/usr/bin/python3
"""Function to return dictionary description of an object for JSON
serialization"""


def class_to_json(obj):
    """Return dictionary of obj attributes for JSON serialization"""
    return obj.__dict__.copy()
