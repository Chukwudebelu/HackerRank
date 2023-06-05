#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import comb as C

if __name__ == "__main__":
  N = int(input())
  _ = input().split(' ')
  K = int(input())

  a_count = _.count('a')
  prob_a = 1 - C(N - a_count, K) / C(N, K)
  print(round(prob_a, 3))
