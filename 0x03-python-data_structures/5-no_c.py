#!/usr/bin/python3
def no_c(my_string):
    word = []
    for letter in my_string:
        word.append(letter)
    my_string = ''
    for letter in word:
        if letter == 'c' or letter == 'C':
            continue
        my_string += letter
    return my_string
