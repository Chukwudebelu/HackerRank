#!/bin/python3
from collections import defaultdict

if __name__ == "__main__":
  n, m = map(int, input().split())
  d = defaultdict(list)
  for i in range(n):
      d[input()].append(i+1)
  for _ in range(m):
      t = input()
      if len(d[t]) == 0:
          print(-1)
      else:
          print(*d[t])
