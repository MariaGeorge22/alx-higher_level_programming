#!/usr/bin/python3
"""Unittest for Rectangle Class
"""
from io import StringIO
import sys
import unittest
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

    def test_str_doc(self):
        """
        Testing __str__() docs exist
        """
        self.assertIsNotNone(Rectangle.__str__.__doc__)
        self.assertNotEqual(Rectangle.__str__.__doc__, "")

    def test_str(self):
        """
        Testing __str__
        """

        captured_output = StringIO()
        sys.stdout = captured_output

        r1 = Rectangle(4, 6, 2, 1, 12)
        print(r1)
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "[Rectangle] (12) 2/1 - 4/6\n")

        captured_output = StringIO()
        sys.stdout = captured_output
        r2 = Rectangle(5, 5, 1)
        print(r2)
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "[Rectangle] (1) 1/0 - 5/5\n")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")


if __name__ == '__main__':
    unittest.main()