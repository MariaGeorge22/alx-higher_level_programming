#!/usr/bin/python3
"""
6th Task
"""


from json import JSONEncoder


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file,
    using a JSON representation
    """
    with open(filename, "w") as file:
        text = JSONEncoder().encode(my_obj)
        content = file.write(text)
        return content
