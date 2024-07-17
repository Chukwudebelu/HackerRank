#!/bin/python3

import os

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def solve(s: str) -> int:
    n = len(s)  # number of digits
    modulo = 1_000_000_007
    
    sum_digits = 0
    for i in range(0, n):
        sum_digits += pow(2, i, modulo) * pow(11, n-1-i, modulo) * (int(s[i]) % modulo)
        
    return (sum_digits % modulo)
    

if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(str(result) + '\n')

    fptr.close()
