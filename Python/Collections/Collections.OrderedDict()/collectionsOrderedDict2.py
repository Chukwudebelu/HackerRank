#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
items = dict()

for _ in range(int(input())):
  *item_list, count = input().split()
  item = ' '.join(item_list) if len(item_list) > 1 else item_list[0]

  if item in items:
      items[item] += int(count)
  else:
      items[item] = int(count)
        
for item, total_cost in items.items():
  print(item, total_cost)
