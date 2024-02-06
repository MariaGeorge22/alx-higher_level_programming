#!/usr/bin/python3
"""
1st Task
"""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout
    """
    with open(filename) as file:
        content = file.read()
        print(content, end="")
