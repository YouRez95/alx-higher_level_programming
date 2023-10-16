#!/usr/bin/python3
""" module """
from models.base import Base


class Rectangle(Base):
    """ class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        self.check_type("width", value)
        self.__width = value

    @property
    def height(self):
        """ get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height """
        self.check_type("height", value)
        self.__height = value

    @property
    def x(self):
        """ get x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set x """
        self.check_type("x", value)
        self.__x = value

    @property
    def y(self):
        """ get y """
        return self.__y

    @y.setter
    def y(self, value):
        """ set y """
        self.check_type("y", value)
        self.__y = value

    def check_type(self, name, value):
        """ check the value """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if (name == "x" or name == "y") and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """ return the area """
        return self.width * self.height

    def display(self):
        """ display the rectangle """
        for i in range(self.height):
            print('#' * self.width)
