#!/bin/python3

import os

#
# Complete the 'strangeGrid' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER r
#  2. INTEGER c
#

def strangeGrid(r, c):
    # if i = 1,2: single digit
    # if i = 3,4: double digit that starts with 1
    # if i = 5,6: double digit that starts with 2
    # odd numbered row: even digits
    # even numbered row: odd digits
  
    row1, row2 = range(0, 8+1, 2), range(1, 9+1, 2)
    row1, row2 = list(map(str, row1)), list(map(str, row2))
  
    if r == 1 or r == 2:
        n = ''
        row = row1 if r == 1 else row2
    elif r % 2 != 0:
        n = r//2
        row = row1
    elif not r % 2:
        n = (r-1)//2
        row = row2
 
    x = lambda a, k: str(n) + a[k]
    for i in range(len(row)):
        row[i] = x(row,i)
    return row[c-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()
