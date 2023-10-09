#!/usr/bin/python3
""" Module """


class BaseGeometry:
    """ my Class """
    def area(self):
        """ area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """ class """
    def __init__(self, width, height):
        """ init """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ return area """
        return self.__width * self.__height

    def __str__(self):
        """ print """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


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

    def __str__(self):
        """ print """
        return "[Square] {}/{}".format(self.__size, self.__size)
