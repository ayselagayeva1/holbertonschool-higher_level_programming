#!/usr/bin/python3
"""Pickle Custom Classes"""

import pickle


class CustomObject:
    """A custom class with attributes and serialization methods."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object and save to a file using pickle.

        Args:
            filename (str): The name of the file to save the object to.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Load and return an object instance from a pickle file.

        Args:
            filename (str): The filename to load the object from.

        Returns:
            CustomObject or None: The loaded object or None on failure.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except (OSError, pickle.PickleError, EOFError):
            return None
