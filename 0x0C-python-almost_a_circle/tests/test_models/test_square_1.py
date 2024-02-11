#!/usr/bin/python3
"""Unittest for Square Class
"""
import unittest
from models.rectangle import Rectangle, __doc__
from models.square import Square, __doc__
from models.base import Base, __doc__
from help_functions.helpers import Helpers


class TestSquareClass(unittest.TestCase):
    """
    Class for Unit Testing Square

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
        self.assertIsNotNone(Square.__doc__)
        self.assertNotEqual(Square.__doc__, "")
        self.assertIsNotNone(Square.__init__.__doc__)
        self.assertNotEqual(Square.__init__.__doc__, "")
        self.assertIsNotNone(Square.__str__.__doc__)
        self.assertNotEqual(Square.__str__.__doc__, "")

    def test_base(self):
        """
        Testing Base Case
        """
        helper = Helpers()

        s1 = Square(5)

        helper.stdout(lambda: print(s1), "[Square] (1) 0/0 - 5\n")

        self.assertEqual(s1.area(), 25)

        helper.stdout(s1.display, """#####
#####
#####
#####
#####
""")

        s2 = Square(2, 2)

        helper.stdout(lambda: print(s2), "[Square] (2) 2/0 - 2\n")

        self.assertEqual(s2.area(), 4)

        helper.stdout(s2.display, """  ##
  ##
""")

        s3 = Square(3, 1, 3)

        helper.stdout(lambda: print(s3), "[Square] (3) 1/3 - 3\n")

        self.assertEqual(s3.area(), 9)

        helper.stdout(s3.display, """


 ###
 ###
 ###
""")

    def test_is_subclass(self):
        """
        check if Square is a subclass of Rectangle
        """
        self.assertTrue(issubclass(Square, Rectangle)
                        and Square is not Rectangle)


if __name__ == '__main__':
    unittest.main()