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

def solve(n, m):
    word_length = m + n - 1
    S = int(math.comb(word_length - 1, m - 1)) % (pow(10, 9) + 7)    
    return (S)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
