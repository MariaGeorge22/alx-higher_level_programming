#!/usr/bin/python3
"""Unittest for Square Class
"""
import unittest
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

    def test_update(self):
        """
        Testing update with validation
        """
        helper = Helpers()

        s1 = Square(5)
        helper.stdout(lambda: print(s1), "[Square] (1) 0/0 - 5\n")

        s1.update(10)
        helper.stdout(lambda: print(s1), "[Square] (10) 0/0 - 5\n")

        s1.update(1, 2)
        helper.stdout(lambda: print(s1), "[Square] (1) 0/0 - 2\n")

        s1.update(1, 2, 3)
        helper.stdout(lambda: print(s1), "[Square] (1) 3/0 - 2\n")

        s1.update(1, 2, 3, 4)
        helper.stdout(lambda: print(s1), "[Square] (1) 3/4 - 2\n")

        s1.update(x=12)
        helper.stdout(lambda: print(s1), "[Square] (1) 12/4 - 2\n")

        s1.update(size=7, y=1)
        helper.stdout(lambda: print(s1), "[Square] (1) 12/1 - 7\n")

        s1.update(size=7, id=89, y=1)
        helper.stdout(lambda: print(s1), "[Square] (89) 12/1 - 7\n")

        with self.assertRaises(AttributeError) as e:
            s1.update(david=5)
            print(s1.david)


if __name__ == '__main__':
    unittest.main()