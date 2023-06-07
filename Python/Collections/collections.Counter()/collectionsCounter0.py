#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

if __name__ == "__main__":
  numShoes = int(input())
  shoeSizes = map(int, input().split())
  numCustomers = int(input())
  
  lst = []
  for _ in range(numCustomers):
    size_price = map(int, input().split())
    lst.append(tuple(size_price))
      
  count_shoeSizes = Counter(list(shoeSizes)) # shoe sizes and counts
  itemsShoe = count_shoeSizes.keys() # shoe sizes only
  shoe_count = count_shoeSizes.values()

  total_money = 0
  for shoe in lst:
    if shoe[0] in itemsShoe and count_shoeSizes[shoe[0]] != 0:
      total_money += shoe[1]
      dict_shoeSizes = dict(count_shoeSizes)
      dict_shoeSizes[shoe[0]] -= 1
      count_shoeSizes = Counter(dict_shoeSizes)
    else:
      total_money += 0
        
  print(total_money)
