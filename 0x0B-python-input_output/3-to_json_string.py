#!/usr/bin/python3
import json
""" module """


def to_json_string(my_obj):
    """ serialization """
    json_string = json.dumps(my_obj)
    return json_string
