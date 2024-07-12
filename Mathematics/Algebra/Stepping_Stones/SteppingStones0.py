#!/bin/python3

import os

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def solve(N: int) -> str:
    i = (-1 + (1 + 8*N)**0.5)/2  # Number of moves
    
    if (int(i) == float(i)):  # Check if i is irrational
        return "Go On Bob" + ' ' + str(int(i))
    else:
        return "Better Luck Next Time"


if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
