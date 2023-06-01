#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

if __name__ == "__main__":
    for k, g in groupby(input()):
        print((len(list(g)), int(k)), end = ' ')
