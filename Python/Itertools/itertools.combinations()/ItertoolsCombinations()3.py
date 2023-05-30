#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools as it

if __name__ == "__main__":
  S, k = input().split()
  for n in range(1, int(k)+1):
      comb = it.combinations(iterable = sorted(S), r = int(n))
      print('\n'.join(''.join(c) for c in comb))
