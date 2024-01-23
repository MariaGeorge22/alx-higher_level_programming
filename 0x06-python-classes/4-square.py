#!/usr/bin/python3

__doc__ = '''
This is the First Task
'''


class Square:
    __doc__ = '''This is a Square Class
    for Defining Squares

    attributes: Size
    '''
    __size = 0

    def __init__(self, size=0) -> None:
        __doc__ = '''This is the init function
                for init the class
                '''
        self.size = size

    def area(self):
        __doc__ = "Calculates the area of the square instance"
        return self.__size ** 2

    @property
    def size(self):
        __doc__ = "returns the size of the square instance"
        return self.__size

    @size.setter
    def size(self, value):
        __doc__ = "sets the size of the square instance"
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
