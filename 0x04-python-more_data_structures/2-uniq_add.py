#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    new_list = list(set(my_list))
    for n in new_list:
        sum += n
    return sum
