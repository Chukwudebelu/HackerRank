#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    x, k = input().split(None)
    
    if eval(input().replace('x', x)) is int(k):
        print(bool(1))  # True
    else:
        print(bool(0))  # False
