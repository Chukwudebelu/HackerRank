#!/bin/python3

import math

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def solve(n: int, m: int) -> int:
    # Write your code here
    word_length = m + n - 1
    
    # N choose R -> N!/(R! * (N-R)!)
    S = int(math.comb(word_length - 1, m - 1))
    
    # No need to compute (N % intmax) or (R % intmax)    
    return S if (S < 10**9 + 7) else (S % (pow(10, 9) + 7)))

if __name__ == '__main__':
    T = int(input().strip())
  
    for _ in range(T):
        m, n = map(int, input().split())
        print(solve(m, n), end = '\n')
