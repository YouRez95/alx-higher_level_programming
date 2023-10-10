#!/usr/bin/python3
""" module """


from json import dumps


def to_json_string(my_obj):
    """ serialization """
    json_string = dumps(my_obj)
    return json_string
