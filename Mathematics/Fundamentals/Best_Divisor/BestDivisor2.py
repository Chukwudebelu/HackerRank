#!/bin/python3

import math
import os
import random
import re
import sys

def best_divisor(n):
    # Generate all possible divisors of the number
    divs = (i for i in range(1, n+1) if n % i == 0)
    
    # Sum all digits of divisors
    best = lambda x: sum(int(i) for i in str(x))
    
    # Find the divisor whose sum is the maximum
    return max(divs, key=best)
    
  
if __name__ == "__main__":
    n = int(input().strip(None))
    print(best_divisor(n))
