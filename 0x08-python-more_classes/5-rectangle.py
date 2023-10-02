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
            height (int): height for rectangle
        """
        self.height = height
        self.width = width

    def area(self):
        """
        Calculate the area of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    @property
    def width(self):
        """
        Get the value of width
        Returns:
            width
        """
        return self.__width

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
        else:
            self.__width = value

    @property
    def height(self):
        """
        Get the value of height
        Returns:
            height
        """
        return self.__height

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
        else:
            self.__height = value

    def __str__(self):
        """
        print our object
        """
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join('#' * self.width for i in range(self.height))

    def __repr__(self):
        """
        print object
        """
        return "Rectangle({}, {})".format(self.width, self.height)
