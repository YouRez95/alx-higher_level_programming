#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
""" Module """


class Square(Rectangle):
    """ class """
    def __init__(self, size):
        """ init """
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ area """
        return self.__size * self.__size
