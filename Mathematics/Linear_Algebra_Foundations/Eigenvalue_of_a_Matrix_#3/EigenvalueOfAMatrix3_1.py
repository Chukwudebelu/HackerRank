#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
def determinant(A: list) -> int:
  return A[0][0]*A[1][1] - A[1][0]*A[0][1]

def matrixSubtract(B: list, A: list) -> list:
  C = [[0, 0], [0, 0]]
  for i in range(len(B)):
    for j in range(len(B[0])):
      C[i][j] = B[i][j] - A[i][j]
  return C

def scalarMultiply(A: list, k: int) -> list:
  Ak = [[0, 0], [0, 0]]
  for i in range(len(A)):
    for j in range(len(A[0])):
      Ak[i][j] = k*A[i][j]
  return Ak

def matrixSquared(A: list) -> list:
  A2 = [[0, 0], [0, 0]]
  for i in range(len(A)):
    for j in range(len(A[0])):
      for k in range(len(A[0])):
        A2[i][j] += A[i][k] * A[k][j]
  return A2

if __name__ == "__main__":
  A = [[2, -1], [-1, 2]]
  I2 = [[1, 0], [0, 1]] # 2 x 2 identity matrix
  
  A2 = matrixSquared(A)
  
  eigval1, eigval2 = -50, -50
  lst_eigvals = []
  
  while (eigval1 < 50):
    val1 = determinant(matrixSubtract(scalarMultiply(I2, eigval1), A))
    if (val1 == 0): # |lambdaI - A| = 0
      lst_eigvals += [eigval1]
    eigval1 += 1
    
  while (eigval2 < 50):
    val2 = determinant(matrixSubtract(scalarMultiply(I2, eigval2), A2))
    if (val2 == 0): # |lambdaI - A| = 0
      lst_eigvals += [eigval2]
    eigval2 += 1
      
  print(*lst_eigvals, sep='\n')
