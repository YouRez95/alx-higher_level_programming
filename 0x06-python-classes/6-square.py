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
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize new instances of square

        args:
            size: size of square
            position: position of square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ set position
            Return:
                position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ set the position
            args:
                value: position
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            for j in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                print('#' * self.__size)
