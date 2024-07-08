#!/bin/python3

def reverseArray(arr):
    a_reversed = list()
    
    for num in arr:
        a_reversed = [num] + a_reversed
        
    return a_reversed


if __name__ == "__main__":
    N, A = input(), []
    
    for a in input().split(None):
        A += [int(a)]
    
    [print(elem, end = ' ') for elem in reverseArray(A)]
