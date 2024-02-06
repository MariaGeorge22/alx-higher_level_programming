#!/usr/bin/python3
"""
4th Task
"""

from json import JSONEncoder


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)
    """
    encoder = JSONEncoder()
    return encoder.encode(my_obj)
