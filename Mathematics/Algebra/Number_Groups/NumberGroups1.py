#!/bin/python3
#
# Complete the 'sumOfGroup' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER k as parameter.
#

def sumOfGroup(k: int) -> int:
    return pow(k, 3)

if __name__ == '__main__':
    k = int(input().rstrip().lstrip())
    answer = sumOfGroup(k)
    print(answer, end = "\n") 
