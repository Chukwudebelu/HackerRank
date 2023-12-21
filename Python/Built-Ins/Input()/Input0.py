#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    x, k = map(int, input().split())
    
    print(True if eval(input()) == k else False)
