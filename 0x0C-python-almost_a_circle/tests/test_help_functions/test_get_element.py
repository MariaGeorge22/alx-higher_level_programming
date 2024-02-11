#!/usr/bin/python3
"""Unittest for get_element
"""
import unittest

from help_functions.get_element import get_element, __doc__


class TestGetElement(unittest.TestCase):
    """
    Class for Unit Testing get_element()

    this class checks for every detail in the class
    """

    def test_docs_exists(self):
        """
        check that docs exist
        """
        self.assertIsNotNone(__doc__)
        self.assertNotEqual(__doc__, "")
        self.assertIsNotNone(get_element.__doc__)
        self.assertNotEqual(get_element.__doc__, "")

    def test_base(self):
        """
        Testing Base Case
        """
        args = [1, 2, 3]
        self.assertEqual(get_element(args, 0, None), 1)

    def test_empty(self):
        """
        Testing empty Case
        """
        args = []
        self.assertIsNone(get_element(args, 0, None))

    def test_out_of_bounds(self):
        """
        Testing out_of_bounds Case
        """
        args = [1, 3]
        self.assertIsNone(get_element(args, 3, None))