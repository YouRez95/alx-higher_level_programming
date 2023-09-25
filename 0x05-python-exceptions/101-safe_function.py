#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
        return result
    except Exception as er:
        sys.stderr.write("Exception: {}\n".format(er))
        return None
