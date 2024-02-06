#!/usr/bin/python3
"""
10th Task
"""


class Student:
    """
    defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializer
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object
        """
        if type(attrs) is list and all(type(i) is str for i in attrs):
            return {key: self.__dict__[key] for key in attrs
                    if key in self.__dict__}
        return self.__dict__
