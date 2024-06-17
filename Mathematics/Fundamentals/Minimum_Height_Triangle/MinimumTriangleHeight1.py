#!/bin/python3
#
# Complete the 'lowestTriangle' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER trianglebase
#  2. INTEGER area
#

def lowestTriangle(b: int, a: int) -> int:
    return ((b + 2 * a - 1) // b)


if __name__ == "__main__":
    base, area = map(int, input().strip().split(' '))
    print(lowestTriangle(base, area))
