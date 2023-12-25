#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
  input()
  list_ = [int(_) for _ in input().lstrip().rstrip().split()]
  print(all(x > 0 for x in list_) and any(x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99] for x in list_))
