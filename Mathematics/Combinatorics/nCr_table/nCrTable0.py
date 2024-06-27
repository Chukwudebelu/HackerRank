#!/bin/python3

import math
import os

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def solve(n: int) -> list:
    mod, lst = 10**9, []
    
    if (n % 2 == 0):    # even (n = 0, 2, 4, ...)
        for r in range(0, n//2+1):
            lst += [math.comb(n, r) % mod]
        return (lst + lst[::-1][1:])
    else:   # odd (n = 1, 3, 5, ...)
        for r in range(0, (n+1)//2):
            lst += [math.comb(n, r) % mod]
        return (lst + lst[::-1])
            

if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
