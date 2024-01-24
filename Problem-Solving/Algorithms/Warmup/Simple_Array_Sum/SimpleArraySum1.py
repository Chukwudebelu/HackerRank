#!/bin/python3
import functools

if __name__ == "__main__":
    ar_length = int(input().strip())
    ar = [int(_) for _ in input().strip(None).split()]
    print(functools.reduce(lambda x, y: x + y, ar))
