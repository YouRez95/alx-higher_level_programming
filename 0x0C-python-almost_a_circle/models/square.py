#!/usr/bin/python3
""" module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class """
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ __str__ """
        return "[Square] ({}) {}/{} - {}".format(
               self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ get size """
        return self.width

    @size.setter
    def size(self, value):
        """ set size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update attr """
        for key, value in kwargs.items():
            if key == "size":
                setattr(self, "width", value)
                setattr(self, "height", value)
            else:
                setattr(self, key, value)
        i = 1
        for arg in args:
            if i == 1:
                self.id = arg
            if i == 2:
                self.width = arg
                self.height = arg
            if i == 3:
                self.x = arg
            if i == 4:
                self.y = arg
            i += 1
