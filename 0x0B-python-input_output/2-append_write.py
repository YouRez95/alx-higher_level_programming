#!/usr/bin/python3
""" module """


def append_write(filename="", text=""):
    """ function for append to a file """
    num_char = 0
    with open(filename, 'a') as f:
        num_char = f.write(text)

    return num_char
