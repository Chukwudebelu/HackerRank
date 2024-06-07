#!/bin/python3

import os

#
# Complete the 'pythagoreanTriple' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER a as parameter.
#

def pythagoreanTriple(a: int) -> tuple:
    if (a % 2 != 0):
        c = ((a**2) + 1)//2
        b = c - 1
    else:
        b = ((a**2)//4) - 1
        c = b + 2
    return (a, b, c)


if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = int(input().strip())

    triple = pythagoreanTriple(a)

    fptr.write(' '.join(map(str, triple)))
    fptr.write('\n')

    fptr.close()
