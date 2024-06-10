#!/bin/python3

import os

#
# Complete the 'sumOfGroup' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER k as parameter.
#

def sumOfGroup(k) -> int:
    return (k * k * k)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    k = int(input().strip())

    answer = sumOfGroup(k)

    fptr.write(str(answer) + '\n')

    fptr.close()
