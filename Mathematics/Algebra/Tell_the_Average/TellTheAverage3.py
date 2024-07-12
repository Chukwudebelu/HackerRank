#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
import operator
    

if __name__== "__main__":  
    N = input('')
    L = input().split(" ")  # L = [a, b, c, ...]
    S_value = 1
    modulo = math.pow(10, 9) + 7   # 1000000007
    
    for _ in L:
        S_value *= (int(_) + 1)
    
    print(operator.mod(S_value - 1, int(modulo)))
