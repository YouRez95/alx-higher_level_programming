#!/usr/bin/python3
"""
    My module to find peak
"""


def find_peak(myList):
    """
       function to find peak from a list
    """
    med = int(len(myList) / 2)
    if not myList:
        return None
    while med < len(myList) - 1 and med > 0:
        if myList[med] >= myList[med-1] and myList[med] >= myList[med+1]:
            return myList[med]
        if myList[med - 1] > myList[med]:
            med = med - 1
        elif myList[med + 1] > myList[med]:
            med = med + 1
    return myList[med]
