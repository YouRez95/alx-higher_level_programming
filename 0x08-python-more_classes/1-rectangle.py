#!/usr/bin/python3
"""
Module:
    Rectangle
"""


class Rectangle:
    """
    class to represent a Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Contructor method for Rectangle
        Args:
            width (int): width of rectangle
            height (height): height for rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Get the value of width
        Returns:
            width
        """
        return self.width

    @width.setter
    def width(self, value):
        """
        set the value of width

        Args:
            value (int): the new value to set

        Raises:
            ValueError: if the value less than 0
            TypeError: if the value not int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the value of height
        Returns:
            height
        """
        return self.height

    @height.setter
    def height(self, value):
        """
        set the value of height

        Args:
            value (int): the new value to set
        Raises:
            ValueError: if the value less than 0
            TypeError: if the value not int
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
