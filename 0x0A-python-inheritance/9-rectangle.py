#!/usr/bin/python3
"""
9st Module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        initializes Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates Rectangle Area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        describes Rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
