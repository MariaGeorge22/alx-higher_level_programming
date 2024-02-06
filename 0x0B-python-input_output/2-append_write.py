#!/usr/bin/python3
"""
3rd Task
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, "a") as file:
        content = file.write(text)
        return content
