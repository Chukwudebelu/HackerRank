#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

if __name__ == "__main__":
  N = int(input().strip())
  x, y = OrderedDict(), []
  
  for _ in range(N):
    item_name, price = input().rsplit(' ', 1)
    x.update([(item_name, int(price))])
    y.append([item_name, int(price)])
    
  for i in y:
    x[i[0]] = y.count(i) * i[1]

  for k in x.items(): print(*k)
