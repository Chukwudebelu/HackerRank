#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

MODULO = 10*10*10*10*10*10*10*10*10 + 7     # 1000000007

def value_of_S_accumulate(L: list) -> int:
    return [*itertools.accumulate(L, lambda a, b: (a + b + a*b) % MODULO)][-1]
    

if __name__== "__main__":
    N = input()
    print(value_of_S_accumulate([int(num) for num in input().split()]))
