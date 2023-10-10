#!/usr/bin/python3
""" module """


from json import load


def load_from_json_file(filename):
    """ function that deserialize data from json file """
    with open(filename, "r") as json_file:
        data = load(json_file)

    return data
