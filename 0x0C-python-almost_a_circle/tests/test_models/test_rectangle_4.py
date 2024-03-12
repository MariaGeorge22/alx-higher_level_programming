#!/usr/bin/python3
"""Unittest for Rectangle Class
"""
from io import StringIO
import sys
import unittest
from models.rectangle import Rectangle, __doc__
from models.base import Base, __doc__
from help_functions.helpers import Helpers


class TestRectangleClass(unittest.TestCase):
    """
    Class for Unit Testing Rectangle

    this class checks for every detail in the class
    """

    def setUp(self):
        # Reset the class ids before each test
        Base.reset_before_tests()

    def test_display_doc(self):
        """
        Testing display() docs exist
        """
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertNotEqual(Rectangle.display.__doc__, "")

    def test_display(self):
        """
        Testing display
        """
        helpers = Helpers()
        captured_output = StringIO()
        sys.stdout = captured_output

        r1 = Rectangle(4, 6)
        r1.display()
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, """####
####
####
####
####
####
""")

        captured_output = StringIO()
        sys.stdout = captured_output
        r1 = Rectangle(2, 2)
        r1.display()
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, """##
##
""")
        r1 = Rectangle(1, 1)
        helpers.stdout(r1.display, "#\n")


if __name__ == '__main__':
    unittest.main()