#!/usr/bin/python3
"""
My module contain one function

Functions:
    text_indentation: print a text with 2 new line ater char
"""


def text_indentation(text):
    """
    print a text with 2 new lines after each of these charactes . : ?

    Args:
        text (str): text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    index = 0
    while index < len(text):
        print(text[index], end="")
        if text[index] == '.' or text[index] == '?' or text[index] == ':':
            print("\n")
            index += 1
        index += 1
