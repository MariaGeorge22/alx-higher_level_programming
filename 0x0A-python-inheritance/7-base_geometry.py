#!/usr/bin/python3
"""
8st Module
"""


class BaseGeometry:
    """
    Empty Class
    """

    def area(self):
        """
        Calculates Area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates the value is int
        and greater than zero
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
