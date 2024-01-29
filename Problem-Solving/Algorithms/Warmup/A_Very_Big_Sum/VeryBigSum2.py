#!/bin/python3

import itertools, operator

def aVeryBigSum(ar: list) -> int:
    return list(itertools.accumulate(ar, operator.add))[-1]

if __name__ == "__main__":
    input(); print(aVeryBigSum(int(_) for _ in input().split()))
