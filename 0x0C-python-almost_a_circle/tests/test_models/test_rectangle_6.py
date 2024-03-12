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

    def test_display_updated(self):
        """
        Testing display after update
        """
        helpers = Helpers()
        captured_output = StringIO()
        sys.stdout = captured_output

        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, """\n\n  ##
  ##
  ##
""")

        captured_output = StringIO()
        sys.stdout = captured_output
        r2 = Rectangle(3, 2, 1, 0)
        r2.display()
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, """ ###
 ###
""")

        r = Rectangle(1, 1)
        helpers.stdout(r.display, "#\n")


if __name__ == '__main__':
    unittest.main()