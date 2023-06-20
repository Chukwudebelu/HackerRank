#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict as od

if __name__ == "__main__":
  n = int(input())
  o_d = od()
  arr = []
  
  for i in range(n):
      item_info = input().split()
      item_name = " ".join(item_info[:len(item_info)-1])
      item_price = int(item_info[len(item_info) - 1])
      arr.append([item_name, item_price])
      o_d.update({item_name: item_price})

  for val in arr:
      o_d[val[0]] = arr.count(val) * val[1]
      
  for val in o_d.keys():
      print(val, str(o_d[val]))
