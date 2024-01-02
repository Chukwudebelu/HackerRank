#!/bin/python3
import re

if __name__ == '__main__':
  strng = input().strip()
  patterns = ['a-z', 'A-Z', '13579', '02468']
  line = ''
  for p in patterns:
    line += ''.join(sorted(re.findall(fr'[{p}]+?', strng)))
  print(line)
