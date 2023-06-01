#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

if __name__ == "__main__":
  S = input().strip(None)
  [print(F"({len(list(c))}, {int(X)})", end = ' ') for X, c in itertools.groupby(S)]
