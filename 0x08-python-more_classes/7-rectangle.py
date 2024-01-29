#!/usr/bin/python3

"""
1st Task Module
"""


class Rectangle:
    """
    Class that defines a rectangle
    """
    __width = 0
    __height = 0
    number_of_instances = 0
    print_symbol = "#"

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0) -> None:
        """
        init function
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    def area(self):
        """
        calculates area
        """
        return self.width * self.height

    def perimeter(self):
        """
        calculates perimeter
        """
        if not self.width or not self.height:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        """
        prints Rectangle
        """
        string = ""
        if self.height and self.width:
            for row in range(self.height):
                for column in range(self.width):
                    string += str(self.print_symbol)
                if row != self.height - 1:
                    string += "\n"
        return string

    def __repr__(self) -> str:
        """
        returns a string rep of Rectangle
        """

        return f"Rectangle({self.width}, {self.height})"

    def __del__(self) -> None:
        """
        behaviour on deleting instance
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
