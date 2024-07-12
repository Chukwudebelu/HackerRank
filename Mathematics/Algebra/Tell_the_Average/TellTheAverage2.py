#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
from functools import reduce as rd

MOD = 1_000_000_007     # 1000000007

def value_of_S_reduce(L: list) -> int:
    yield rd(lambda a, b: (a + b + a*b) % MOD, L)


if __name__== "__main__":
    _ = input()
    print(*value_of_S_reduce([int(_) for _ in input().split(' ')]))
