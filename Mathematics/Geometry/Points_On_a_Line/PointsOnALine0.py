#!/bin/python3

import math
import os
import random
import re
import sys


def pointsOnALine(x, y):
    # x = #: vertical -, y = #: horizontal -
    return 'Yes'.upper() if len(set(x)) == 1 or len(set(y)) == 1 else 'No'.upper()

if __name__ == '__main__':
    n = int(input())
    X = list(); Y = list()
     
    for n_itr in range(n):
        xy = input().split()
        x = int(xy[0])
        y = int(xy[1])
        X.append(x)
        Y.append(y)
        
    print(pointsOnALine(X, Y))
