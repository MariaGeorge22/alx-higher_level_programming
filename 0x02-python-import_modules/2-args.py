#!/usr/bin/python3
import sys


if __name__ == "__main__":
    args = sys.argv
    num_args = len(args) - 1
    str_num = f"{num_args} " +\
        f"{'argument' if num_args == 1 else 'arguments'}" +\
        f"{':' if num_args > 0 else '.'}"
    print(str_num)
    for arg in range(num_args):
        print(f"{arg+1}: {args[arg+1]}")
