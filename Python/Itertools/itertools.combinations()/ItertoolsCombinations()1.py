#!/bin/python3
from itertools import combinations

if __name__ == "__main__":
  S, k = input().split()
  lst = []
  for i in range(1, int(k)+1):
      lst.append(list(combinations(sorted(S), i)))
  for i in lst:
      print('\n'.join(''.join(j) for j in i))
