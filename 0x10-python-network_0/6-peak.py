#!/usr/bin/python3
"""
    My module to find peak
"""


def find_peak(myList):
    """
       function to find peak from a list
    """

    if not myList:
        return None
    if len(myList) == 1:
        return myList[0]
    med = int(len(myList) / 2)
    if myList[med] > myList[med-1] and myList[med] > myList[med+1]:
        return myList[med]
    if myList[med - 1] > myList[med]:
        return find_peak(myList[:med])
    else:
        return find_peak(myList[med+1:])
