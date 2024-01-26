#!/usr/bin/python3
"""
Module for first task
Using Tests to check task if successful

"""


def add_integer(a, b=98) -> int:
    """
    This Function adds 2 numbers

    params: a
            b (optional)
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return a+b
