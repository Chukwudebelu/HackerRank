#!/bin/python3

import math

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def solve(n: int) -> str:
    moves = (math.pow(1 + 8*n, .5) - 1)/2
    
    if (moves % 1):   # Check if floating point number: 0.000...
        return 'Better Luck Next Time'
    return 'Go On Bob %d' % (moves)


if __name__ == "__main__":
    T = int(input().strip())

    list_of_Ns = []

    for t in range(T):
        list_of_Ns += [int(input())]

    print(*map(solve, list_of_Ns), sep = '\n')
