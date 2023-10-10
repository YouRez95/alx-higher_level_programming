#!/usr/bin/python3
""" module """


def pascal_triangle(n):
    """ pascal triangle """
    myList = [] 
    if n <= 0:
        return myList
    for i in range(0, n):
        prevList = []
        if i == 0:
            prevList.append(1)
            myList.append(prevList)
