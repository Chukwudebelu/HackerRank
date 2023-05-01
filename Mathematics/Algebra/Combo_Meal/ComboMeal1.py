#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'profit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER b
#  2. INTEGER s
#  3. INTEGER c
#

def profit(b: int, s: int, c: int) -> int:
    return (b + s) - c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        s = int(first_multiple_input[1])

        c = int(first_multiple_input[2])

        result = profit(b, s, c)

        fptr.write(str(result) + '\n')

    fptr.close()
