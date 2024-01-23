#!/usr/bin/python3

__doc__ = '''
This is the First Task
'''


class Square:
    __doc__ = '''This is a Square Class
    for Defining Squares

    attributes: None
    '''

    def __init__(self) -> None:
        __doc__ = '''This is the init function
                for init the class
                '''
        pass


print(Square.__init__.__doc__)
