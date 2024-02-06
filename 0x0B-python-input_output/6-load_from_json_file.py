#!/usr/bin/python3
"""
7th Task
"""


from json import JSONDecoder


def load_from_json_file(filename):
    """
    reads a text file (UTF8) and prints it to stdout
    """
    with open(filename) as file:
        content = file.read()
        return JSONDecoder().decode(content)
