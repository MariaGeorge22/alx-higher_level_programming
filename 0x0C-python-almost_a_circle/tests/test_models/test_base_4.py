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

    def test_from_json_string_doc(self):
        """
        Testing docs exist
        """
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertNotEqual(Base.from_json_string.__doc__, "")

    def test_from_json_string(self):
        """
        Testing from_json_string()
        """
        helpers = Helpers()
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        helpers.stdout(lambda: print("[{}] {}".format(type(list_input), list_input)),
                       "[<class 'list'>] [{'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': 1, 'height': 7}]\n")
        helpers.stdout(lambda: print("[{}] {}".format(type(json_list_input), json_list_input)),
                       '[<class \'str\'>] [{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]\n')
        helpers.stdout(lambda: print("[{}] {}".format(type(list_output), list_output)),
                       "[<class 'list'>] [{'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': 1, 'height': 7}]\n")

    def test_is_empty(self):
        """
        Test Empty Case
        """
        self.assertEqual(Rectangle.from_json_string(""), [])
        self.assertEqual(Rectangle.from_json_string(None), [])


if __name__ == '__main__':
    unittest.main()