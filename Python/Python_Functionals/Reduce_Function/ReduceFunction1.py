#!/bin/python3
from fractions import Fraction
from functools import reduce
import math

def product(fracs: list):
    t = math.prod(fracs, start = 1)
    return (t.numerator, t.denominator)

if __name__ == "__main__":
    fracs = list()
    for _ in range(int(input())):
        fracs += [Fraction([int(_) for _ in input().split())]
    result = product(fracs)
    print(*result)
