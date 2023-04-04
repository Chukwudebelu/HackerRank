import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER m
#

def solve(a, m):
    # check if a % m is a perfect square
    # return 'YES' if pow(a % m, 1/2) == int(math.sqrt(a % m)) and math.gcd(a,m)==1 else 'NO'
    if m == 2 or a == 0:
      return "YES"
    elif pow(a, (m-1)//2, m) == 1:
      return "YES"
    else:
      return "NO"
   
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = solve(a, m)

        fptr.write(result + '\n')

    fptr.close()
