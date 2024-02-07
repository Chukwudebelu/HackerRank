#!/bin/python3

import os

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s: int, t: int, a: int, b: int, apples: list, oranges: list) -> list:
    count_Apples = 0; validOranges = 0
    for j in apples:
        if (s <= j + a <= t):
            count_Apples += 1
    for k in oranges:
        if (s <= k + b <= t):
            validOranges += 1
    return [count_Apples, validOranges]

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    for _ in countApplesAndOranges(s, t, a, b, apples, oranges):
        print(_)
