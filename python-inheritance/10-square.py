#!/usr/bin/python3
"""
10-square module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""

    def __init__(self, size):
        """Initialize size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """String representation"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
