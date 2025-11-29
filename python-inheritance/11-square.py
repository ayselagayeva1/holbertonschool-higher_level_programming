#!/usr/bin/python3
"""Create square with the help of rectangle class """

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class for creating Square"""

    def __init__(self, size):
        """Initialize size with private atribute"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Implemented area method """
        return self.__size ** 2

    def __str__(self):
        """Return the print answer"""
        return f"[Square] {self.__size}/{self.__size}"
