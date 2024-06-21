#!/bin/python3

from operator import *
#
# Complete the 'solve' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def solve(n: int, m: int):
    return sub(mul(n, m), 1)

if __name__ == "__main__":
    n, m = input().lstrip().rstrip().split(' ')
    print(solve(n, m), end = '\n')
