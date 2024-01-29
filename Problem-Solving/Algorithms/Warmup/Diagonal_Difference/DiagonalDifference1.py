#!/bin/python3

def diagonalDifference(A: list) -> int:
    n, sum_d = len(A), 0
    for i in range(n):
        sum_d += (A[i][i] - A[i][n-1-i])
    return sum_d if (sum_d >= 0) else -sum_d
            
if __name__ == "__main__":
    n = int(input())
    arr = [[int(k) for k in input().split(' ')] for _ in range(n)]
    print(diagonalDifference(arr))
