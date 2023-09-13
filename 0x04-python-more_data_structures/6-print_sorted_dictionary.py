#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_keys = list(a_dictionary)
    for key in sorted(list_keys):
        print("{} : {}".format(key, a_dictionary[key]))
