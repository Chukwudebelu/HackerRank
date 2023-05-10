#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    M = [[1, 2, 3], [2, 3, 4], [1, 1, 1]]
    N = [[4, 5, 6], [7, 8, 9], [4, 5, 7]]
    
    a1 = [1, 2, 3]
    a2 = [2, 3, 4]
    a3 = [1, 1, 1]
    matrix_a = [a1, a2, a3]

    b1 = [4, 5, 6] 
    b2 = [7, 8, 9]
    b3 = [4, 5, 7]
    matrix_b = [b1, b2, b3]

    c1 = [0, 0, 0]
    c2 = [0, 0, 0]
    c3 = [0, 0, 0]
    matrix_c = [c1, c2, c3]

    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]

    for n in range(len(matrix_c)):
        for i in range(len(matrix_c[n])):
            print(matrix_c[n][i])
