#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_keys = [key for key in a_dictionary]
    list_keys.sort()
    for key in list_keys:
        print("{} : {}".format(key, a_dictionary[key]))
