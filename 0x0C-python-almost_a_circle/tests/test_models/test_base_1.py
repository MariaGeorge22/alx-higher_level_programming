#!/usr/bin/python3
"""Unittest for Base Class
"""
import unittest
from models.base import Base, __doc__


class TestBaseClass(unittest.TestCase):
    """
    Class for Unit Testing Base

    this class checks for every detail in the class
    """

    def setUp(self):
        # Reset the class ids before each test
        Base.reset_before_tests()

    def test_class_doc(self):
        """
        Testing docs exist
        """
        self.assertIsNotNone(__doc__)
        self.assertNotEqual(__doc__, "")
        self.assertIsNotNone(Base.__doc__)
        self.assertNotEqual(Base.__doc__, "")
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertNotEqual(Base.__init__.__doc__, "")

    def test_base(self):
        """
        Testing Base Case
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_private(self):
        """
        Testing accessibilty of private attrib
        """
        b1 = Base()
        with self.assertRaises(AttributeError):
            b1.__nb_objects
        with self.assertRaises(AttributeError):
            Base.__nb_objects


if __name__ == '__main__':
    unittest.main()