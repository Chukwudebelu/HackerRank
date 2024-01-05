#!/bin/python3
import math

cube = lambda x: int(math.pow(x, 3))

def fibonacci(n):
    lst = [0 for _ in range(n)]
    lst[1] = 1
    for i in range(0, n-2):
        lst[i+2] = lst[i] + lst[i+1]
    return lst[0:n:1]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
