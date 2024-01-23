#!/usr/bin/python3

__doc__ = '''
This is the First Task
'''


class Node:
    __doc__ = '''This is a Node Class
    for Defining Nodes

    attributes: data, next_node
    '''
    __data = None
    __next_node = None

    def __init__(self, data, next_node=None):
        __doc__ = "Initializer"
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        __doc__ = 'data getter'
        return self.__data

    @data.setter
    def data(self, value):
        __doc__ = 'data setter'
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        __doc__ = 'next_node getter'
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        __doc__ = 'next_node setter'
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    __doc__ = '''This is a SinglyLinkedList Class
    for Defining SinglyLinkedLists

    attributes: head
    '''
    __head = None

    def __init__(self):
        __doc__ = "Initializer"

    def __str__(self) -> str:
        __doc__ = "gets string"
        string = ""
        current = self.__head
        while current is not None:
            string += str(current.data)+"\n"
            current = current.next_node
        if string.endswith("\n"):
            string = string[:-1]
        return string

    def sorted_insert(self, value):
        __doc__ = "insert in sorted list"
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        else:
            current = self.__head
            if current.data > value:
                new_node.next_node = current
                self.__head = new_node
            else:
                while current.next_node is not None and \
                        current.next_node.data <= value:
                    current = current.next_node
                new_node.next_node = current.next_node
                current.next_node = new_node
