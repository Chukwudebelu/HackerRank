#!/bin/python3
from fractions import Fraction
from functools import reduce
import operator

def product(fracs: list) -> list:
    '''
    Use the .mul() method in the operator module to 
    perform multiplication (a * b)
    '''
    Fr = reduce(operator.mul, fracs)
    return list((Fr.numerator, Fr.denominator))

if __name__ == "__main__":
    fracs = list()
    for _ in range(int(input())):
        fracs += [Fraction([int(_) for _ in input().split())]
    result = product(fracs)
    print(*result)
