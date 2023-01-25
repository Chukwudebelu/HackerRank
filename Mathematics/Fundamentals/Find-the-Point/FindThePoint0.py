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

def findPoint(px, py, qx, qy):
    dx = abs(qx - px)
    dy = abs(qy - py)
    
    if qx == px and qy == py:
        rx = qx
        ry = qy
    elif qx == px:
        rx = qx
        sgn_y = (qy - py)/dy
        ry = qy + (sgn_y * dy)
    elif qy == py:
        sgn_x = (qx - px)/dx
        rx = qx + sgn_x * dx
        ry = qy
    else:
        sgn_x = (qx - px)/dx
        sgn_y = (qy - py)/dy
        rx = qx + sgn_x * dx
        ry = qy + sgn_y * dy
    
    return [str(int(rx)), str(int(ry))]

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
