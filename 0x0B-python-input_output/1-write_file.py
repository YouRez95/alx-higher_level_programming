#!/usr/bin/python3
""" module """


def write_file(filename="", text=""):
    """ function for written to a file """
    num_char = 0
    with open(filename, 'w') as f:
        num_char = f.write(text)

    return num_char
