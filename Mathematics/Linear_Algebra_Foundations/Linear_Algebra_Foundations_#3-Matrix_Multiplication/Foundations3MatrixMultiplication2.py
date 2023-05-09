# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
  matrix1 = [[1, 2], [2, 3]]
  matrix2 = [[4, 5], [7, 8]]
  elem = 0
  
  for i in range(len(matrix1)): # row in 1st matrix
    for j in range(len(matrix2[0])): # column in 2nd matrix
        for k in range(len(matrix2)): # position index
            elem += matrix1[i][k] * matrix2[k][j]
        print(elem)
        elem = 0
