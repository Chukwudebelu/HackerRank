#!/bin/python3
cube = lambda z: z * z * z

def fibonacci(n):
    seq = list()
    for k in range(n):
        if (k == 0 or k == 1):
            seq += [k]
        else:
            seq += [seq[k-1] + seq[k-2]]
    return seq

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
