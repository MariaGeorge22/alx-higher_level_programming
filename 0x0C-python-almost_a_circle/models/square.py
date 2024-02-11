#!/usr/bin/python3
"""
Class Rectangle inherits from Base.
"""
from help_functions.get_element import get_element
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializer
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        creates the string rep
        of a Square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        size getter
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        size setter
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        updates the self instanse
        """
        if args:
            self.id = get_element(args, 0, self.id)
            self.size = get_element(args, 1, self.size)
            self.x = get_element(args, 2, self.x)
            self.y = get_element(args, 3, self.y)
        else:
            for key, value in kwargs.items():
                if key in ["id", "size", "x", "y"]:
                    setattr(self, key, value or getattr(self, key))

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle
        """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y,
        }