#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
  S = input().rstrip().lstrip()
  
  count = 0
  i = 0
  s = S[i]
  
  while (0 <= i < len(S)):
    if s == S[i]:
      count += 1      
    else:
      print((count, int(s)), end = ' ')
      s = S[i]
      count = 1
    i += 1
  
  print((count, int(s)))
