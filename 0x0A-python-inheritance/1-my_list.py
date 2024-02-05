#!/usr/bin/python3
"""
2st Module
"""


class MyList(list):
    """
    Custom list Class
    """

    def print_sorted(self):
        """
        that prints the list, but sorted
        """
        print(sorted(self))
