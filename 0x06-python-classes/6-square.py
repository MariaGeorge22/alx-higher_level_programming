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
    __position = 0

    def __init__(self, size=0, position=(0, 0)) -> None:
        __doc__ = '''This is the init function
                for init the class
                '''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        __doc__ = "returns the position of the square instance"
        return self.__position

    @position.setter
    def position(self, value):
        __doc__ = "sets the position of the square instance"
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        __doc__ = "prints the square instance in ##"
        if self.__size == 0:
            print("")
        else:
            for x in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for y in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
