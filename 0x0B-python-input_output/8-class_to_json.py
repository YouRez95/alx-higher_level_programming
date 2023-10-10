#!/usr/bin/python3
""" module """


def class_to_json(obj):
    """ return __dict__ """
    return vars(obj)
