#!/bin/python3
# Without using the Regex Module

if __name__ == "__main__":
    T = int(input().strip(None)) # Number of Test Cases
  
    for _ in range(0, T):
        try:
            print(bool(float(str(input()))))
        except ValueError:
            print("False")
