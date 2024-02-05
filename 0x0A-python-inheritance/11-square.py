#!/usr/bin/python3
"""
9st Module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    inherits from BaseGeometry
    """

    def __init__(self, size):
        """
        initializes Square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        describes Square
        """
        return f"[Square] {self.__size}/{self.__size}"
