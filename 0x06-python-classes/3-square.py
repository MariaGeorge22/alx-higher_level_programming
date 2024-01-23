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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        __doc__ = "Calculates the area of the square instance"
        return self.__size ** 2
