#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
        exit(0)
    if sys.argv[2] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
        exit(0)
    if sys.argv[2] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
        exit(0)
    if sys.argv[2] == '/':
        if b == 0:
            exit(1)
        print("{} / {} = {}".format(a, b, div(a, b)))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
