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

    def test_update_updated(self):
        """
        Testing update after update
        """
        captured_output = StringIO()
        sys.stdout = captured_output

        r1 = Rectangle(10, 10, 10, 10)
        print(r1)
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "[Rectangle] (1) 10/10 - 10/10\n")
        captured_output = StringIO()
        sys.stdout = captured_output

        r1.update(height=1)
        print(r1)
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "[Rectangle] (1) 10/10 - 10/1\n")

        captured_output = StringIO()
        sys.stdout = captured_output

        r1.update(width=1, x=2)
        print(r1)
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "[Rectangle] (1) 2/10 - 1/1\n")

        captured_output = StringIO()
        sys.stdout = captured_output

        r1.update(y=1, width=2, x=3, id=89)
        print(r1)
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "[Rectangle] (89) 3/1 - 2/1\n")

        captured_output = StringIO()
        sys.stdout = captured_output

        r1.update(x=1, height=2, y=3, width=4)
        print(r1)
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "[Rectangle] (89) 1/3 - 4/2\n")

        captured_output = StringIO()
        sys.stdout = captured_output

        r1.update(99, height=3)
        print(r1)
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "[Rectangle] (99) 1/3 - 4/2\n")

    def test_validation(self):
        """
        check validation
        """
        r1 = Rectangle(10, 10, 10, 10)

        with self.assertRaises(TypeError) as e:
            r1.update(height="1")
            self.assertEqual(str(e.exception), "height must be an integer")

        with self.assertRaises(AttributeError) as e:
            r1.update(david=5)
            print(r1.david)


if __name__ == '__main__':
    unittest.main()