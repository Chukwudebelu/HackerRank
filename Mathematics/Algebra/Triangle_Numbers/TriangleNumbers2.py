#!/bin/python3
#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def solve(n: int) -> int:
    return [3, 2, 4, 2][n % 4]

if __name__ == "__main__":
    T = int(input('').strip(None))

    [(print(solve(int(input().strip())))) for t in range(0, T)]
