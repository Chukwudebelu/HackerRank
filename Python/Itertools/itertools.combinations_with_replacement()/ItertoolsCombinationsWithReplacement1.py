#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement as comb_r

if __name__ == "__main__":
    string_k = input().split()
    S = sorted(string_k[0])
    k = int(string_k[1])
    
    print(*[''.join(i) for i in comb_r(S, k)], sep='\n')
