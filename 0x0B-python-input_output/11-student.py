#!/usr/bin/python3
""" module """


class Student:
    """ class Student """
    def __init__(self, first_name, last_name, age):
        """ init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to json """
        my_dict = {}
        if attrs is not None:
            for attr in attrs:
                if hasattr(self, attr):
                    my_dict[attr] = getattr(self, attr)
            return my_dict
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }

    def reload_from_json(self, json):
        """ reload from json """
        for item in json:
            setattr(self, item, json[item])
