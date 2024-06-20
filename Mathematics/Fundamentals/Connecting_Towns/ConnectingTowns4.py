#!/bin/python3
from itertools import accumulate
import operator

def connectingTowns(n, routes) -> int:
    return [*accumulate(routes, operator.mul)][-1] % 1234567

if __name__ == "__main__":
    T = int(input())
    routesAll = [connectingTowns(len([int(_) for _ in input().split()])+1,[int(_) for _ in input().split()]) for t in range(T)]
    print(*routesAll, sep = '\n')
    
