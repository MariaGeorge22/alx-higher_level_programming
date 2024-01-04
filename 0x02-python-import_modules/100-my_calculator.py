#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


if __name__ == "__main__":
    args = sys.argv
    num_args = len(args)-1
    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(args[1])
    b = int(args[3])
    sign = args[2]
    res = 0
    if ['+', '-', '*', '/'].count(sign) == 0:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if sign == '+':
        res = add(a, b)
    if sign == '-':
        res = sub(a, b)
    if sign == '*':
        res = mul(a, b)
    if sign == '/':
        res = div(a, b)
    print(f"{a:d} {sign} {b:d} = {res:d}")
