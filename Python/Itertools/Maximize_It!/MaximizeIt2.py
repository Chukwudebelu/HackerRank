#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == "__main__":
    K, M = list(map(int, input().split()))
    
    lst = [list(map(int, input().split()))[1:] for _ in range(K)]
    
    xPow2 = lambda x: x**2
    
    lst2 = [list(map(xPow2, i)) for i in lst]
    
    print(max([sum(j) % M for j in product(*lst2)]))
