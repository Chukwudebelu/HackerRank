#!/bin/python3
#
# Complete the 'connectingTowns' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY routes
#

def connectingTowns(n, routes) -> int:
    """
    Calculate the total number of possible paths from town 1 to town n (mod 1234567).
    """
    res = 1
    for i in routes:
        res = (res * i) % 1234567
    return res


if __name__ == "__main__":
    T = int(input().strip())

    for t in range(T):
        n = int(input().strip())
        routes = [*map(int, input().rstrip().split(' '))]
        print(connectingTowns(n, routes), end = '\n')
