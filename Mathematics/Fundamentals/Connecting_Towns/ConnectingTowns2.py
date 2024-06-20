#!/bin/python3

from functools import reduce
from operator import mul

def connectingTowns(n, routes) -> int:
    # Take the product of all possible paths (mod 1234567)
    return reduce(mul, routes) % 1234567


if __name__ == "__main__":
    for _ in range(int(input())):
        n = input(''); routes = [int(r) for r in input().rstrip().split(None)]
        print(connectingTowns(int(n), routes))
