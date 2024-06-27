#!/bin/python3

from math import comb

def solve(n: int) -> list:
    return [comb(n, r) % 10**9 for r in range(0, n+1)]

if __name__ == "__main__":
    T = int(input().strip(None))

    for t in range(T):
        n = int(input().strip())
        print(*solve(n), sep = ' ', end = '\n')
