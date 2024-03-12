#!/usr/bin/python3
"""Unittest for Base Class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from help_functions.helpers import Helpers


class TestBaseClass(unittest.TestCase):
    """
    Class for Unit Testing Base

    this class checks for every detail in the class
    """

    def setUp(self):
        # Reset the class ids before each test
        Base.reset_before_tests()

    def test_to_json_string_doc(self):
        """
        Testing docs exist
        """
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertNotEqual(Base.to_json_string.__doc__, "")

    def test_to_json_string(self):
        """
        Testing to_json_string()
        """
        helpers = Helpers()
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertDictEqual(dictionary,
                             {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})
        self.assertEqual(type(dictionary), dict)

        self.assertEqual(type(json_dictionary), str)
        helpers.stdout(lambda: print(json_dictionary),
                       '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]\n')

    def test_empty(self):
        """
        Testing Empty
        """
        helpers = Helpers()
        helpers.stdout(lambda: print(Base.to_json_string([])),
                       '[]\n')
        helpers.stdout(lambda: print(Base.to_json_string(None)),
                       '[]\n')


if __name__ == '__main__':
    unittest.main()