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

    def test_area_doc(self):
        """
        Testing area() docs exist
        """
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertNotEqual(Rectangle.area.__doc__, "")

    def test_area(self):
        """
        Testing Area
        """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)


if __name__ == '__main__':
    unittest.main()