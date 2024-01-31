#!/bin/python3

if __name__ == "__main__":
  _ = int(input().lstrip().rstrip())
  arr = input().split(' ')
  pos_, neg_, zer_ = [0]*3

  for num in arr:
    if (num > '0'):
      pos_ = pos_ + 1
    elif (num < '0'):
      neg_ = neg_ + 1
    else:
      zer_ = zer_ + 1

  print("%.6f\n"*3 % (pos_/_, neg_/_, zer_/_), end='')
