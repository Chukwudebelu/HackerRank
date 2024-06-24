#!/bin/python3

import os

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY points as parameter.
#

def solve(points: list) -> bool:
    # Extract the coordinate tripes: (x, y, z)
    p1, p2, p3, p4 = points
    
    # x, y, & z coordinates of each point
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    x3, y3, z3 = p3
    x4, y4, z4 = p4
    
    # Check for equality
    return ("YES" if ((x1 == x2 and x2 == x3 and x3 == x4) or (y1 == y2 and y2 == y3 and y3 == y4) or (z1 == z2 and z2 == z3 and z3 == z4)) else "NO")
        

if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):

        points = []

        for _ in range(4):
            points.append(list(map(int, input().rstrip().split())))

        result = solve(points)

        fptr.write(result + '\n')

    fptr.close()
