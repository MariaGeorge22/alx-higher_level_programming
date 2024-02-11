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

    def test_create_doc(self):
        """
        Testing docs exist
        """
        self.assertIsNotNone(Base.create.__doc__)
        self.assertNotEqual(Base.create.__doc__, "")

    def test_create(self):
        """
        Testing create()
        """
        helpers = Helpers()
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        helpers.stdout(lambda: print(r1), "[Rectangle] (1) 1/0 - 3/5\n")
        helpers.stdout(lambda: print(r2), "[Rectangle] (1) 1/0 - 3/5\n")
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_create_missing(self):
        """
        test create without some attributes
        """
        helpers = Helpers()
        r = Rectangle.create()
        helpers.stdout(lambda: print(r), "[Rectangle] (1) 0/0 - 1/1\n")


if __name__ == '__main__':
    unittest.main()