#!/usr/bin/python3
"""Unittest for Base Class
"""
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
        for path in ["Rectangle.json", "Square.json"]:
            if os.path.exists(path):
                os.remove(path)

    def test_save_to_file_doc(self):
        """
        Testing docs exist
        """
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertNotEqual(Base.save_to_file.__doc__, "")

    def test_save_to_file(self):
        """
        Testing save_to_file()
        with overwriting
        """
        helpers = Helpers()
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            helpers.stdout(lambda: print(file.read()),
                           '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}, {"x": 0, "y": 0, "id": 2, "height": 4, "width": 2}]\n')

        r2 = Rectangle(3, 4)
        Rectangle.save_to_file([r2])

        with open("Rectangle.json", "r") as file:
            helpers.stdout(lambda: print(file.read()),
                           '[{"x": 0, "y": 0, "id": 3, "height": 4, "width": 3}]\n')

        r2 = Square(3)
        Square.save_to_file([r2])

        with open("Square.json", "r") as file:
            helpers.stdout(lambda: print(file.read()),
                           '[{"id": 4, "x": 0, "size": 3, "y": 0}]\n')

    def test_empty_array(self):
        """
        Test Empty array
        """
        helpers = Helpers()

        Rectangle.save_to_file(list())

        with open("Rectangle.json", "r") as file:
            helpers.stdout(lambda: print(file.read()),
                           '[]\n')

        Square.save_to_file(list())

        with open("Square.json", "r") as file:
            helpers.stdout(lambda: print(file.read()),
                           '[]\n')

    def test_empty(self):
        """
        Test Empty Case
        """
        helpers = Helpers()
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            helpers.stdout(lambda: print(file.read()),
                           '[]\n')

        Square.save_to_file(None)

        with open("Square.json", "r") as file:
            helpers.stdout(lambda: print(file.read()),
                           '[]\n')


if __name__ == '__main__':
    unittest.main()