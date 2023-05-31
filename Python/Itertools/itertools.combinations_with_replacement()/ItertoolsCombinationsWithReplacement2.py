#!/bin/python3
from itertools import combinations_with_replacement

inputs = input().split()
S, k = sorted(inputs[0]), int(inputs[1])
print('\n'.join(map(''.join, combinations_with_replacement(S, k))))
