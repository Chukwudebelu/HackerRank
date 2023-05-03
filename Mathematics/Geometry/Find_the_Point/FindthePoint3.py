#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findPoint' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER px
#  2. INTEGER py
#  3. INTEGER qx
#  4. INTEGER qy
#

def findPoint(px: int, py: int, qx: int, qy: int) -> list:
    x_distance: int = qx - px
    y_distance: int = qy - py
    
    rx: int = qx + x_distance
    ry: int = qy + y_distance
    
    r: list[int, int] = [rx, ry]
    
    return r

if __name__ == '__main__':
    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        px = int(first_multiple_input[0])

        py = int(first_multiple_input[1])

        qx = int(first_multiple_input[2])

        qy = int(first_multiple_input[3])

        result = findPoint(px, py, qx, qy)

        print(' '.join(map(str, result)))
