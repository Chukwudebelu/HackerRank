#!/bin/python3

from functools import reduce

def connectingTowns(n, routes):
    return reduce(lambda x, y: x*y, routes) % 1234567

if __name__ == "__main__":
    T, t = int(input().strip(None)), 0
    while (t < T):
        n = int(input().strip(None))
        routes = map(int, input().lstrip().rstrip().split())
        result = connectingTowns(n, list(routes))
        print(result)
        t += 1
