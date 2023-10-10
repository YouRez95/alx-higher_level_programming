#!/usr/bin/python3
""" Module """


def read_file(filename=""):
    """ function for read file """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
