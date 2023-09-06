#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    strc = ""
    target = 0
    for i in str:
        if target == n:
            target += 1
            continue
        strc += i
        target += 1
    return strc
