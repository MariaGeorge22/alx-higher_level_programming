#!/usr/bin/python3
"""
Class Rectangle inherits from Base.
"""
from models.base import Base
from help_functions.get_element import get_element


class Rectangle(Base):
    """
    Rectangle Class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializer
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        width setter
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        height setter
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        x setter
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        y setter
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        returns the area value
        of the Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """
        prints in stdout
        the Rectangle instance
        with the character #
        """
        str = ""
        str += "\n" * self.y
        for i in range(self.height):
            str += " " * self.x
            str += "#" * self.width
            if i < self.height - 1:
                str += "\n"
        print(str)

    def __str__(self):
        """
        creates the string rep
        of a Rectangle
        """
        return f"[Rectangle] " +\
            f"({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        updates the Rectangle instance
        """
        if args:
            self.id = get_element(args, 0, self.id)
            self.width = get_element(args, 1, self.width)
            self.height = get_element(args, 2, self.height)
            self.x = get_element(args, 3, self.x)
            self.y = get_element(args, 4, self.y)
        else:
            for key, value in kwargs.items():
                if key in ["id", "width", "height", "x", "y"]:
                    setattr(self, key, value or getattr(self, key))

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle
        """
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width,
        }
