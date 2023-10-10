#!/usr/bin/python3
""" module """


from json import loads


def from_json_string(my_str):
    """ deserialization """
    return loads(my_str)
