#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == "__main__":
    K, M= [int(_) for _ in input().split()]
    i = [[int(_) for _ in input().split()[1:]] for k in range(K)]

    combs = product(*i)

    def fun(c):
        return sum([i**2 for i in c]) % M

    print(max([fun(c) for c in combs]))
