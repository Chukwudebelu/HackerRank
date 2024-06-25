#!/bin/python3
#
# Complete the 'solve' function below.
# 
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY steps as parameter.
#

def solve(steps) -> int:
    min_x, min_y = [10**6 + 1]*2
    
    for i in range(len(steps)):
        if steps[i][0] < min_x:
            min_x = steps[i][0]
        if steps[i][1] < min_y:
            min_y = steps[i][1]
    return (min_x * min_y)
    

if __name__ == "__main__":
    N = int(input().strip(None))
    steps = list()
    for _ in range(N):
        steps += [[*map(int, input().rstrip().split())]]
    print(solve(steps), end = '\n')
