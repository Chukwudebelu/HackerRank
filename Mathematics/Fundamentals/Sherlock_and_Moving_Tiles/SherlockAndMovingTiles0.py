#!/bin/python3

import os
from math import sqrt

#
# Complete the 'movingTiles' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER s1
#  3. INTEGER s2
#  4. INTEGER_ARRAY queries
#

def movingTiles(l, s1, s2, queries):
    A1, A2 = map(lambda x: x**2, [l, l])
    c1 = c2 = (l/2)*sqrt(2) # 0
    times = []
    for q_i in queries:
        t = (l*sqrt(2) - sqrt(2*q_i))/abs(s1-s2)
        times.append(t)
    return times


if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    l = int(first_multiple_input[0])

    s1 = int(first_multiple_input[1])

    s2 = int(first_multiple_input[2])

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = movingTiles(l, s1, s2, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
