#!/bin/python3

import os

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def solve(n: int) -> int:
    if (n % 2 == 1):
        return 2
    if (n % 4 == 0):
        return 3
    return 4


if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for t in range(T):
        n = int(input().strip())

        result = solve(n)

        fptr.write(str(result) + '\n')

    fptr.close()
