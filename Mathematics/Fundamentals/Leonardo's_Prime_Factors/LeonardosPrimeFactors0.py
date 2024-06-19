#!/bin/python3

import math

#
# Complete the 'primeCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def primeCount(n: int):
    # Write your code here
    # count the number of distinct prime factors of any number in the range [1,n]
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
    
    prod, count = 1, 0
    while (prod <= n):
        prod *= primes[count]
        count += 1
    return count-1
  

if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
