#!/usr/bin/python3
def magic_string():
    magic_string._s = getattr(magic_string, "_s", "BestSchool,") + "BestSchool"
    return magic_string._s
