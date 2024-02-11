#!/usr/bin/python3
"""Unittest for Square Class
"""
import unittest

from help_functions.helpers import Helpers
from models.square import Square, __doc__
from models.base import Base, __doc__


class TestSquareClass(unittest.TestCase):
    """
    Class for Unit Testing Square

    this class checks for every detail in the class
    """

    def setUp(self):
        # Reset the class ids before each test
        Base.reset_before_tests()

    def test_to_dictionary_doc(self):
        """
        Testing to_dictionary() docs exist
        """
        self.assertIsNotNone(Square.to_dictionary.__doc__)
        self.assertNotEqual(Square.to_dictionary.__doc__, "")

    def test_to_dictionary(self):
        """
        Testing to_dictionary()
        """
        helpers = Helpers()

        s1 = Square(10, 2, 1)
        helpers.stdout(lambda: print(s1), "[Square] (1) 2/1 - 10\n")
        s1_dictionary = s1.to_dictionary()
        self.assertDictEqual(
            s1_dictionary, {'x': 2, 'y': 1, 'id': 1, 'size': 10})
        self.assertEqual(type(s1_dictionary), dict)
        helpers.stdout(lambda: print(s1_dictionary),
                       "{'id': 1, 'x': 2, 'size': 10, 'y': 1}\n")
        s2 = Square(1, 1)
        helpers.stdout(lambda: print(s2), "[Square] (2) 1/0 - 1\n")
        s2.update(**s1_dictionary)
        helpers.stdout(lambda: print(s2), "[Square] (1) 2/1 - 10\n")
        self.assertNotEqual(s1, s2)


if __name__ == '__main__':
    unittest.main()