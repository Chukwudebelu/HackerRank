#!/bin/python3

import math
import os
import random
import re
import sys

def athleteSort(A, k):
  return sorted(A, key = lambda x: x[k])

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    for i in athleteSort(arr, k):
      print(*i)
