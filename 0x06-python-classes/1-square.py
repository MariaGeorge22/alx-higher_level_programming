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

    def __init__(self, size=None) -> None:
        __doc__ = '''This is the init function
                for init the class
                '''
        if size is not None:
            self.__size = size
