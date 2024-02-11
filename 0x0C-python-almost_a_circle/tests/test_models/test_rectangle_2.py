#!/usr/bin/python3
"""Unittest for Rectangle Class
"""
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

    def test_validators_doc(self):
        """
        Testing validators docs exist
        """
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertNotEqual(Rectangle.width.__doc__, "")
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertNotEqual(Rectangle.height.__doc__, "")
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertNotEqual(Rectangle.x.__doc__, "")
        self.assertIsNotNone(Rectangle.y.__doc__)
        self.assertNotEqual(Rectangle.y.__doc__, "")

    def test_validation(self):
        """
        Testing Validation
        """
        with self.assertRaises(TypeError) as verror:
            Rectangle(10, "2")
        self.assertEqual(str(verror.exception), "height must be an integer")
        with self.assertRaises(ValueError) as verror:
            r = Rectangle(-10, 2)
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError) as verror:
            r.width = -10
        self.assertEqual(str(verror.exception), "width must be > 0")
        with self.assertRaises(TypeError) as terror:
            r.x = {}
        self.assertEqual(str(terror.exception), "x must be an integer")
        with self.assertRaises(ValueError) as verror:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(verror.exception), "y must be >= 0")


if __name__ == '__main__':
    unittest.main()