#!/bin/python3

if __name__ == "__main__":
  _ = input().strip()
  arr = input().split(' ')
  pos_, neg_, zer_ = [0]*3

  for num in arr:
    if (num > '0'):
      pos_ = pos_ + 1
    elif (num < '0'):
      neg_ = neg_ + 1
    else:
      zer_ = zer_ + 1

  print("%.6f\n%.6f\n%.6f\n" % (pos_, neg_, zer_)
