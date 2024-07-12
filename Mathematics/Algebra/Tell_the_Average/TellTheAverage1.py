#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

def value_of_S_iterative(L: list) -> int:
    while (len(L) > 1):
        a, b = L[0], L[1]
        L.remove(L[1])  # Delete 2nd element: L[1]
        L[0] += b + a*b
        
    return L[0] % (pow(10, 9) + 7)
    
        
if __name__ == "__main__":
    N = input().strip(None)
    _list_ = list(map(int, input().split(' ')))
    print(value_of_S_iterative(_list_))
