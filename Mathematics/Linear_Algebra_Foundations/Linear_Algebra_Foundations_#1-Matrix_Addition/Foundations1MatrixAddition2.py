# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
  """
  a1, a2, a3 = [1, 2, 3], [2, 3, 4], [1, 1, 1]
  b1, b2, b3 = [4, 5, 6], [7, 8, 9], [4, 5, 7]
  """
  print(*[1+4, 2+5, 3+6, 2+7, 3+8, 4+9, 1+4, 1+5, 1+7], sep='\n')
