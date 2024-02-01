#!/bin/python3
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    n = len(arr)
    store_sum = []
    for i in range(n):
        store_sum.append(sum(arr[:i] + arr[i+1:]))
        
    store_sum.sort()
    print(store_sum[0], store_sum[-1])

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
