#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
def determinant(A: list) -> int:
  a, b, c = A[0]
  det1 = a*(A[1][1]*A[2][2] - A[2][1]*A[1][2])
  det2 = -b*(A[1][0]*A[2][2] - A[2][0]*A[1][2])
  det3 = c*(A[1][0]*A[2][1] - A[2][0]*A[1][1])
  return det1 + det2 + det3

def matrixSubtract(B: list, A: list) -> list:
  C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  for i in range(len(B)):
    for j in range(len(B[0])):
      C[i][j] = B[i][j] - A[i][j]
  return C

def scalarMultiply(A: list, k: int) -> list:
  Ak = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  for i in range(len(A)):
    for j in range(len(A[0])):
      Ak[i][j] = k * A[i][j]
  return Ak


if __name__ == "__main__":
  A = [[1, -3, 3], [3, -5, 3], [6, -6, 4]]
  I3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]] # 3 x 3 identity matrix

  eigval = -10
  lst_eigvals = []
  
  while (eigval < 20):
    val = determinant(matrixSubtract(scalarMultiply(I3, eigval), A))
    if (val == 0): # |lambda*I - A| = 0
      lst_eigvals += [eigval]
    eigval += 1
      
  print(*lst_eigvals, sep='\n')
