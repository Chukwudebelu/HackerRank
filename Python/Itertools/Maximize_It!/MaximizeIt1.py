#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == "__main__":
    K, M = list(map(int, input().split()))
    
    lst = []    
    for k in range(K):
        lst.append(list(map(int, input().split()))[1:])
        
    square = lambda x: x * x # lambda x: x*x
    
    lst2 = []
    for i in lst:
        lst2.append(list(map(square, i)))
        
    maxval = []
    for j in list(product(*lst2)):
        maxval.append(sum(j) % M)
        
    print(max(maxval))
