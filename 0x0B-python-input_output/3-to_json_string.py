#!/usr/bin/python3
from json import dumps
""" module """


def to_json_string(my_obj):
    """ serialization """
    json_string = dumps(my_obj)
    return json_string
