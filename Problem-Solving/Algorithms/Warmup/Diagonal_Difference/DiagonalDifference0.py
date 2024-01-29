#!/bin/python3

import os

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr: list) -> int:
    # Sum the primary diagonal
    sum_pd = 0
    for i in range(len(arr)):
      sum_pd += arr[i][i]
    
    # Sum the secondary diagonal
    sum_sd = 0
    for j in range(len(arr)):
      sum_sd += arr[j][len(arr)-j-1]
    
    return abs(sum_pd - sum_sd)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
