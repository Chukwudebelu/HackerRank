#!/bin/python3

import math
import os
from fractions import Fraction
#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#

def solve(a: int, b: int, c: int):
    # Write your code here
    if (c >= a + b):
        return "1/1"
    else:
        big_triangle = c ** 2
        if (c > a):
            big_triangle -= (c-a)**2 
        if (c > b):
            big_triangle -= (c-b)**2 
        frac = Fraction(big_triangle, 2 * a * b)
        den, num = frac.denominator, frac.numerator
        ans = f"{num}/{den}"
    return ans

if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        c = int(first_multiple_input[2])

        result = solve(a, b, c)

        fptr.write(result + '\n')

    fptr.close()
