#!/usr/bin/python3

""" Module
This is a module for creating a new class
Classes:
    Square: class represent a square
"""


class Square:
    """ class representing a square
    This class alows us to create and manipulate square
    Attributes:
        size: size of square
    """
    def __init__(self, size=0):
        """ Initialize new instances of square

        args:
            size: size of square
        """
        
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
