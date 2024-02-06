#!/usr/bin/python3
"""
5th Task
"""

from json import JSONDecoder, JSONEncoder


def from_json_string(my_str):
    """
    returns the JSON representation of an object (string)
    """
    decoder = JSONDecoder()
    return decoder.decode(my_str)
