#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby as gb

if __name__ == "__main__":
    print(*[(len(list(g)), int(k)) for k, g in gb(input())])
