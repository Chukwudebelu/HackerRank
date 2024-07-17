#!/bin/python3

import operator as op

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def solve(s: str) -> int:
    subsequence_sum = 0
    MOD = pow(10, 9) + 7    # 1000000007
    
    for j in range(0, len(s)):
        powersOf2 = pow(2, j, MOD)
        powersOf11 = pow(11, len(s)-1-j, MOD)
        digit = pow(int(s[j]), 1, MOD)
        subsequence_sum = op.add(subsequence_sum, powersOf2 * powersOf11 * digit)
        subsequence_sum = op.mod(subsequence_sum, MOD)
    yield subsequence_sum
    

if __name__ == "__main__":
    print(*solve(input('').strip()))
