#!/bin/python3

import os

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s: str) -> int:
    # Write your code here
    count = 1 if s[0].isupper() else 1
    
    for i in range(1,len(s)):
        if s[i].isupper():
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
