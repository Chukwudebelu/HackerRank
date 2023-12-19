#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    N, X = map(int, input().split(' ', 2))
    
    lst = []
    for i in range(X):
        vals = map(float, input().split())
        lst.append(list(vals))
        
    for j in zip(*lst):
      print(f'{sum(j) / X:.1f}')
