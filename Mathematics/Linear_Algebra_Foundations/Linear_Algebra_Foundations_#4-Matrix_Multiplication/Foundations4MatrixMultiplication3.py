#!/bin/python3

if __name__ == "__main__":
    M = [[1, 2, 3], [2, 3, 4], [1, 1, 1]]
    N = [[4, 5, 6], [7, 8, 9], [4, 5, 7]]
    elem = 0
    
    for i in range(len(M)):
        for j in range(len(N[i])):
            for k in range(len(N)):
                elem += M[i][k] * N[k][j]
            print(elem); elem = 0
