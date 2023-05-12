#!/bin/python3
import math

if __name__ == "__main__":
  n = 100;
  A = [[1, math.pow(n, 1/n), 1, 0, 1]]

  for i in A:
      for q in i:
          print(math.floor(q**n))
