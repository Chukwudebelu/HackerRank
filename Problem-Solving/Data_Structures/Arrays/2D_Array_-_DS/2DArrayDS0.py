#!/bin/python3

import os

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr: list):
    hour_array = []
    dummy = []
    for j in range(len(arr)-2):
        hour_array.append(dummy)
    
        for i in range(len(arr[j])-2):
            hour_glass_sum = sum(arr[j][i:i+3]) + arr[j+1][i+1] + sum(arr[j+2][i:i+3])
            dummy.append(hour_glass_sum)
            
            max_sum = max(dummy)
                
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
