#!/bin/python3
from fractions import Fraction
from functools import reduce

def product(fracs: list) -> tuple:
    '''
    Calculate the product using the built-in .__mul__ 
    method/attribute for fractions.Fraction objects
    '''
    frac = reduce(Fraction.__mul__, fracs)
    return frac.numerator, frac.denominator

if __name__ == "__main__":
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
