#!/usr/bin/python3
def uppercase(str):
    for n in str:
        print("{}".format(chr(ord(n) - 32)
                          if ord(n) > 96 and ord(n) < 123 else n), end="")
    print("")
