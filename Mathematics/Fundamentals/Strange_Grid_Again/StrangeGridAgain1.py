#!/bin/python3
#
# Complete the 'strangeGrid' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER r
#  2. INTEGER c
#

def strangeGrid(r: int, c: int) -> int:
    if (r % 2): return 10*(r//2) + 2*(c-1) # odd
    else: return 10*((r-1)//2) + 2*c-1 # even
      

if __name__ == "__main__":
    params = [int(_) for _ in input().lstrip().rstrip().split(' ')]
    r, c = params
    print(strangeGrid(r, c), end = '\n')
