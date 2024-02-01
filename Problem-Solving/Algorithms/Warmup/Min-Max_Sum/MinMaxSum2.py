#!/bin/python3
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr: list) -> None:
    arr.sort(reverse=0)
    print(sum(arr[0:len(arr)-1:]), sum(arr[1::]))

if __name__ == "__main__":
    miniMaxSum([*map(int, input().split())])
