#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
def matrixPower(A, k):
    row, col = len(A), len(A[0])
    if (k == 1):
        # base
        return A
    elif (k > 1):
        # recursive
        A_less_1 = matrixPower(A,k-1)
        last_A = A
        B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
        for i in range(len(A_less_1)):
            for j in range(len(A_less_1[0])):
                for k in range(len(last_A)):
                    B[i][j] += A_less_1[i][k] * last_A[k][j]
        return B            
  
if __name__ == "__main__":
    A = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
    Apow100 = matrixPower(A, 100)
    A1, A2, A3 = Apow100
    A, B, _ = A1
    _, C, _ = A2
    _, D, E = A3
    print(A, B, C, D, E, sep='\n')
