#!/bin/python3
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr: list) -> tuple:
    min_sum, max_sum = [0]*2
    arr = sorted(arr, reverse=False)
    n = arr.__len__()
    for i in range(n-1):
        min_sum += arr[i]
        max_sum += arr[i+1]
    return (min_sum, max_sum)

if __name__ == '__main__':
    arr = [int(_) for _ in input().split(' ')]
    print(*miniMaxSum(arr), sep=' ')
