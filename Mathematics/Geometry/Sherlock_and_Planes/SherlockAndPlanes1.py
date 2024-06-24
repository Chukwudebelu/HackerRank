#!/bin/python3
#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY points as parameter.
#

def solve(points) -> int:
    p1, p2, p3, p4 = points
        
    # Check for equality in the x, y, or z-coordinates
    if ((p1[0] == p2[0] == p3[0] == p4[0]) or (p1[1] == p2[1] == p3[1] == p4[1]) or (p1[2] == p2[2] == p3[2] == p4[2])):
        return "yes".upper()
    else:
        return "no".upper()
        

if __name__ == "__main__":
    T = int(input().strip(None))

    for t_itr in range(T):
        points = list()
        for _ in range(4):
            points += [[*map(int, input().rstrip().split())]]
        result = solve(points)
        print(result, end = '\n')
