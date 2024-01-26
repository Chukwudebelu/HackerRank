#!/bin/python3

import functools

def aVeryBigSum(ar):
    # Write your code here
    return functools.reduce(lambda x, y: x + y, ar)

if __name__ == '__main__':
    _ = input()
    ar = [*map(int, input().split(" "))]
    print(aVeryBigSum(ar))
