#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
  n = int(input())
  arr  = input().split()
  print(any([arr[i] == arr[i][::-1] for i in range(len(arr))]) and all([int(arr[i]) > 0 for i in range(len(arr))]))
