#!/usr/bin/python3
"""Defines a BaseGeometry class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Make class from BaseGeometry Class"""

    def __init__(self, width, height):
        """Initalize width and height numbers"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Calculate area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Calculate the print answer"""
        return f"[Rectangle] {self.__width}/{self.__height}"
