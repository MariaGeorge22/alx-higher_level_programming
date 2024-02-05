#!/usr/bin/python3
"""
9st Module
"""


class MyInt(int):
    """
    inherits from int
    is a rebel
    """

    def __eq__(self, __value: object) -> bool:
        """
        returns self != __value
        """
        return super().__ne__(__value)

    def __ne__(self, __value: object) -> bool:
        """
        returns self == __value
        """
        return super().__eq__(__value)
