#!/bin/python3

from math import factorial
import os

def handshake(n: int) -> int:
    if (n == 1):
        return 0
    else:
        return int(factorial(n)/(factorial(n-2)*2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = handshake(n)

        fptr.write(str(result) + '\n')

    fptr.close()
