if __name__ == "__main__":
  A = [
    [1, 2, 3],
    [2, 3, 4],
    [1, 1, 1]
  ]
  B = [
    [4, 5, 6],
    [7, 8, 9],
    [4, 5, 0]
  ]
  
  i = 0 # row index
  j = 0 # column index
  
  for row in A:
    for a in row:
      print(a - B[i][j])  # a = A[i][j]
      j += 1              # Go to next column
    j = 0                 # Restart at the 1st column
    i += 1                # Go to next row
