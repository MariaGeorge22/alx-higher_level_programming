#!/usr/bin/python3
"""
9st Module
"""


def add_attribute(obj, name, value):
    """
    adds a new attribute to an object
    if it’s possible
    """
    if not hasattr(obj, '__dict__') or hasattr(obj, name):
        raise TypeError("can't add new attribute")
    return setattr(obj, name, value)
