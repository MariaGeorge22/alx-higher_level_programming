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

    def test_class_doc(self):
        """
        Testing docs exist
        """
        self.assertIsNotNone(__doc__)
        self.assertNotEqual(__doc__, "")
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertNotEqual(Rectangle.__doc__, "")
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertNotEqual(Rectangle.__init__.__doc__, "")

    def test_base(self):
        """
        Testing Base Case
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(10, 2, 1, 5, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 1)
        self.assertEqual(r3.y, 5)

    def test_private(self):
        """
        Testing accessibilty of private attrib
        """
        b1 = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            b1.__nb_objects
        with self.assertRaises(AttributeError):
            b1.__width
        with self.assertRaises(AttributeError):
            b1.__height
        with self.assertRaises(AttributeError):
            b1.__x
        with self.assertRaises(AttributeError):
            b1.__y
        with self.assertRaises(AttributeError):
            Rectangle.__nb_objects

    def test_init_validation(self):
        """
        Testing validation
        """
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle("1", 1)
            self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(0, 1)
            self.assertEqual(str(e.exception), "width must be > 0")
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, "1")
            self.assertEqual(str(e.exception), "height must be an integer")
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(1, 0)
            self.assertEqual(str(e.exception), "height must be > 0")
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 1, "0")
            self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(1, 1, -1)
            self.assertEqual(str(e.exception), "x must be >= 0")
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 1, 1, "-1")
            self.assertEqual(str(e.exception), "y must be an integer")
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(1, 1, 1, -1)
            self.assertEqual(str(e.exception), "y must be >= 0")

    def test_is_subclass(self):
        """
        check if Rectangle is a subclass of Base
        """
        self.assertTrue(issubclass(Rectangle, Base) and Rectangle is not Base)

    def test_getters_setters(self):
        """
        check if getters/setters work
        """
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)


if __name__ == '__main__':
    unittest.main()