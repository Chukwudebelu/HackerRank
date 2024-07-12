#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
sys.setrecursionlimit(10**6)

def value_of_S_recursive(L: list) -> int:
    n = len(L)
    if (n == 0):    # empty list: L = []
        return 0
    elif (n == 1):  # unary list: L = [a]
        return L[0]
    else:           # other lists: L = [a, b, ...]
        a = L[0]
        b = L[1]
        del L[1]    # L.pop(1) or L.remove(L[1])
        L[0] = (a + b + a*b) % (10**9 + 7)
        return value_of_S_recursive(L)

        
if __name__ == "__main__":
    N = int(input(''))
    List = [int(_) for _ in input().split(' ')]
    print(value_of_S_recursive(List))
