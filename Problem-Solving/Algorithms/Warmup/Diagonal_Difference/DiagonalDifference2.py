#!/bin/python3

if __name__ == "__main__":
    m = int(input())
    Ar = [[*map(int, input().split())] for _ in range(m)]
    print(abs(sum([Ar[i][i] - Ar[i][m-1-i] for i in range(m)])))
