#!/bin/python3

if __name__ == "__main__":
    M = [[1, 2, 3], [2, 3, 4], [1, 1, 1]]
    N = [[4, 5, 6], [7, 8, 9], [4, 5, 7]]
    
    lst = []
    for row in M:
        for i in range(len(row)-2):
            lst += [row[i]*N[0][0] + row[i+1]*N[1][0] + row[i+2]*N[2][0]]
            lst += [row[i]*N[0][1] + row[i+1]*N[1][1] + row[i+2]*N[2][1]]
            lst += [row[i]*N[0][2] + row[i+1]*N[1][2] + row[i+2]*N[2][2]]
    print(*lst, sep='\n')
