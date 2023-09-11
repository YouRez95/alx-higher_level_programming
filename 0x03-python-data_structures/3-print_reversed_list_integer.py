#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for index in range(len(my_list)):
        print("{:d}".format(my_list[len(my_list) - index - 1]))
