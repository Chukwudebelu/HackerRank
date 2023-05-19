#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
def determinant(A: list[list[int]]) -> int:
  return A[0][0]*A[1][1] - A[1][0]*A[0][1]

def matrixSubtract(B, A):
  C = [[0, 0], [0, 0]]
  for i in range(len(B)):
    for j in range(len(B[0])):
      C[i][j] = B[i][j] - A[i][j]
  return C

def scalarMultiply(A, k: int):
  Ak = [[0, 0], [0, 0]]
  for i in range(len(A)):
    for j in range(len(A[0])):
      Ak[i][j] = k*A[i][j]
  return Ak


if __name__ == "__main__":
  A = [[0, 1], [-2, -3]]
  I2 = [[1, 0], [0, 1]] # 2 x 2 identity matrix

  eigval = -10
  lst_eigvals = []
  
  while (eigval < 5):
    val = determinant(matrixSubtract(scalarMultiply(I2, eigval), A))
    if (val == 0): # |λI - A| = 0
      lst_eigvals += [eigval]
    eigval += 1
      
  print(*lst_eigvals, sep='\n')
