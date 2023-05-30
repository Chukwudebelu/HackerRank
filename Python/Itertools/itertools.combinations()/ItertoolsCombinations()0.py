#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == "__main__":
    S, k = input().split()
    
    for j in range(1, int(k)+1):
        print(*[''.join(list(i)) for i in list(combinations(sorted(S), j))], sep = '\n')
