#!/bin/python3

import os

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    len_a = len(a)
    len_b = len(b)
    
    count_a = count_b = 0
    
    for i in range(len_a):
        if a[i] > b[i]: 
            count_a += 1
        elif a[i] < b[i]:
            count_b += 1
        else:
            pass
    return [count_a, count_b]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
