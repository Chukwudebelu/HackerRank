#!/bin/python3

import math
import os
import random
import re
import sys

def best_div(n):
    lst = [i for i in range(1, n+1) if not n % i]
    sum_dgts = list()
    for j in map(str, lst): 
        sum_dgts.append(sum(*[map(int,list(j))]))

    return lst[sum_dgts.index(max(sum_dgts))]


if __name__ == "__main__":
    n = int(input().strip())
    print(best_div(n))
