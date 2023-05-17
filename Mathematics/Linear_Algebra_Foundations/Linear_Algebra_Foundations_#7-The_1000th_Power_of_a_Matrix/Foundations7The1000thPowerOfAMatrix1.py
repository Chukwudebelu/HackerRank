#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

def powerMatrix(A, k):
  '''kth power of a 2 x 2 square matrix'''
  if (k == 0):
    I2 = [[1, 0], [0, 1]] # 2 x 2 identity matrix
    return I2
    
  if (k == 1): # base
    return A
  elif (k > 1): # recursive
    A_less_1 = powerMatrix(A, k-1)
    A_last = A
    B = [[0, 0], [0, 0]]
    for i in range(len(A_less_1)):
      for j in range(len(A_less_1[0])):
        for l in range(len(A_last)):
          B[i][j] += A_less_1[i][l] * A_last[l][j]
    return B
    
if __name__ == "__main__":
  n = 1000; A = [[-2, -9], [1, 4]]
  A500 = powerMatrix(A, 500)
  A1000 = powerMatrix(A500, 2)
  [print(*i, sep='\n') for i in A1000]
