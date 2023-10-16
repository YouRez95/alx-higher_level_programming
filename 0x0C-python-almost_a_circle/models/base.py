#!/usr/bin/python3
""" Module """
import json


class Base:
    """ My class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to_json """
        if list_dictionaries is None:
            return "[]"
        json_string = json.dumps(list_dictionaries)
        return json_string
