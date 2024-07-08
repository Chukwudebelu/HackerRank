#!/bin/python3
#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    # Using List Comprehension
    return [a[x] for x in range(len(a)-1,-1,-1)]

if __name__ == "__main__":
    arr_size = int(input().lstrip().rstrip())

    arr = [int(_) for _ in input().rstrip().split(' ')]

    print(*reverseArray(arr))
