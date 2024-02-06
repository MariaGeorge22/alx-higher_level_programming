#!/usr/bin/python3
"""
2nd Task
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, "w") as file:
        content = file.write(text)
        return content
