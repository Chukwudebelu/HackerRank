#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
  S = input().replace(" ", "")
  count = 1
  i = 0
  
  for i in range(len(S)-1):
    if S[i] == S[i+1]:
      count += 1      
    else:
      print((count, int(S[i])), end = ' ')
      count = 1
    i += 1
  print((count,int(S[i])))
