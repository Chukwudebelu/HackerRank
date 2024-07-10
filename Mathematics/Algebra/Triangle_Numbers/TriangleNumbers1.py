#!/bin/python3

import os

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def solve(n):
    # One-liner equivalent code of TriangleNumbers0.py
    return -1 if (n < 3) else 2 if (n % 4 == 1 or n % 4 == 3) else 3 if (n % 4 == 0) else 4
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(str(result) + '\n')

    fptr.close()
