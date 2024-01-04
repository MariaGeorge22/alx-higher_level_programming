#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sum = 0
    args = sys.argv
    num_args = len(args)
    for arg in range(1, num_args):
        sum += int(args[arg])
    print(sum)
