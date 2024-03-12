#!/usr/bin/python3
"""Unittest for Rectangle Class
"""
import unittest

from help_functions.helpers import Helpers
from models.rectangle import Rectangle, __doc__
from models.base import Base, __doc__


class TestRectangleClass(unittest.TestCase):
    """
    Class for Unit Testing Rectangle

    this class checks for every detail in the class
    """

    def setUp(self):
        # Reset the class ids before each test
        Base.reset_before_tests()

    def test_to_dictionary_doc(self):
        """
        Testing to_dictionary() docs exist
        """
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)
        self.assertNotEqual(Rectangle.to_dictionary.__doc__, "")

    def test_to_dictionary(self):
        """
        Testing to_dictionary()
        """
        helpers = Helpers()

        r1 = Rectangle(10, 2, 1, 9)
        helpers.stdout(lambda: print(r1), "[Rectangle] (1) 1/9 - 10/2\n")
        r1_dictionary = r1.to_dictionary()
        self.assertDictEqual(
            r1_dictionary, {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
        helpers.stdout(lambda: print(r1_dictionary),
                       "{'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}\n")
        self.assertEqual(type(r1_dictionary), dict)

        r2 = Rectangle(1, 1)
        helpers.stdout(lambda: print(r2), "[Rectangle] (2) 0/0 - 1/1\n")
        r2.update(**r1_dictionary)
        helpers.stdout(lambda: print(r2), "[Rectangle] (1) 1/9 - 10/2\n")
        self.assertNotEqual(r1, r2)


if __name__ == '__main__':
    unittest.main()