#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

if __name__ == "__main__":
  X = int(input()) # # of shoes
  shoe_sizes = input().split(' ') # list of all shoe sizes
  N = int(input()) # # of customers
  
  C = collections.Counter(shoe_sizes) # shoe sizes & price of shoe
  total_price =  0
  for _ in range(N):
    shoe_size, cost = input().split(' ')
    if C[shoe_size] > 0:
      total_price += int(cost)
      C[shoe_size] -= 1
    else:
      total_price += 0
  print(total_price)
