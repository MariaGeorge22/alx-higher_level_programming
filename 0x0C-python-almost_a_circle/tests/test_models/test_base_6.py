#!/usr/bin/python3
"""Unittest for Base Class
"""
from genericpath import exists
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from help_functions.helpers import Helpers


class TestBaseClass(unittest.TestCase):
    """
    Class for Unit Testing Base

    this class checks for every detail in the class
    """

    def setUp(self):
        # Reset the class ids before each test
        Base.reset_before_tests()

    def test_load_from_file_doc(self):
        """
        Testing docs exist
        """
        self.assertIsNotNone(Base.load_from_file.__doc__)
        self.assertNotEqual(Base.load_from_file.__doc__, "")

    def test_load_from_file(self):
        """
        Testing load_from_file()
        """
        helpers = Helpers()
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        rect = list_rectangles_input[0]
        helpers.stdout(lambda: print(rect), "[Rectangle] (1) 2/8 - 10/7\n")
        rect = list_rectangles_input[1]
        helpers.stdout(lambda: print(rect), "[Rectangle] (2) 0/0 - 2/4\n")

        rect = list_rectangles_output[0]
        helpers.stdout(lambda: print(rect), "[Rectangle] (1) 2/8 - 10/7\n")
        rect = list_rectangles_output[1]
        helpers.stdout(lambda: print(rect), "[Rectangle] (2) 0/0 - 2/4\n")

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        square = list_squares_input[0]
        helpers.stdout(lambda: print(square), "[Square] (5) 0/0 - 5\n")
        square = list_squares_input[1]
        helpers.stdout(lambda: print(square),
                       "[Square] (6) 9/1 - 7\n")

        square = list_squares_output[0]
        helpers.stdout(lambda: print(square),
                       "[Square] (5) 0/0 - 5\n")
        square = list_squares_output[1]
        helpers.stdout(lambda: print(square),
                       "[Square] (6) 9/1 - 7\n")

    def test_not_exist(self):
        """
        test response on no file
        """
        for file in ["Rectangle.json", "Square.json"]:
            if exists(file):
                os.remove(file)

        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])


if __name__ == '__main__':
    unittest.main()