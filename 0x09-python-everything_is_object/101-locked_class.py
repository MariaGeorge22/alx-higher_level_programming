#!/usr/bin/python3
"""
Optional Task 2 Module
"""


class LockedClass:
    """
    LockedClass
    only the "first_name" attribute is allowed
    """

    def __getattribute__(self, __name: str):
        """
        Overriding the attribute setter
        """
        if __name == "first_name":
            object.__getattribute__(self, __name)
        else:
            raise AttributeError(
                f"'LockedClass' object has no attribute '{__name}'")

    def __setattr__(self, key, value):
        """
        Overriding the attribute setter
        """
        if key == "first_name":
            object.__setattr__(self, key, value)
        else:
            raise AttributeError(
                f"'LockedClass' object has no attribute '{key}'")
