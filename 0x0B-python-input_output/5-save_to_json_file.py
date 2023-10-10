#!/usr/bin/python3
""" module """


from json import dump


def save_to_json_file(my_obj, filename):
    """ function that serialize data and save it to json file """
    with open(filename, "w") as json_file:
        dump(my_obj, json_file)
