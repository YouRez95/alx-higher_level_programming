#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            end = "\n" if i == x - 1 else ""
            print(my_list[i],  end=end)
        except Exception:
            print("", end="\n")
            return i
    return x
