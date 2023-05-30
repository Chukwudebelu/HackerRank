#!/bin/python3
from itertools import combinations as comb

if __name__ == "__main__":
  # Read the string, S and all possible combinations, k
  string_n = input().split(' ')
  S = string_n[0]
  k = int(string_n[1])
  lst = []

  # Loop for all possible combinations <= k
  i = 1
  while (i <= k):
    lst += [*comb(sorted(S), i)]
    i += 1
    
  # Print each combination as a string
  for c in lst:
    print(''.join(c))
