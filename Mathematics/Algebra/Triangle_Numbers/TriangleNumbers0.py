#!/bin/python3

import os

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def solve(n: int) -> int:
    cond = (n % 4)  # Pattern repeats every 4 steps
    if (n < 3):
        return -1
    elif (cond == 1 or cond == 3):
        return 2
    elif not (cond):
        return 3
    elif (cond == 2):
        return 4
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(str(result) + '\n')

    fptr.close()
