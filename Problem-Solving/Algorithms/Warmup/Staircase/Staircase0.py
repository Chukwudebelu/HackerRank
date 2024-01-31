#!/bin/python3
#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n: int) -> None:
    # Write your code here
    for i in range(1,n+1):
        print(('#'*i).rjust(n), end='\n')
        
if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)
