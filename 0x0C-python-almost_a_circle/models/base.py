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

    @staticmethod
    def from_json_string(json_string):
        """ to origin type """
        if json_string is None:
            return []
        data = json.loads(json_string)
        return data

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file """
        my_objects = []
        if list_objs is not None:
            for obj in list_objs:
                my_objects.append(obj.to_dictionary())
        to_file = cls.to_json_string(my_objects)
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, 'w') as f:
            f.write(to_file)
