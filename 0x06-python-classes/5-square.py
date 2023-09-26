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

    @property
    def size(self):
        """  get the size of square
         Returns:
             size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """  set the size of square
             args:
                 value: size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """  Caluculate the area of square
         Returns:
             the area
        """
        return self.__size * self.__size

    def my_print(self):
        """ print the square with the character #
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print('#' * self.__size)
