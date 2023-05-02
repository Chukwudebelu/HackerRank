# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
  a1, a2, a3 = [1, 2, 3], [2, 3, 4], [1, 1, 1]
  b1, b2, b3 = [4, 5, 6], [7, 8, 9], [4, 5, 7]
  c1, c2, c3 = [], [], []
  for i in range(len(a1)):
    c1.append(a1[i] + b1[i])
    c2.append(a2[i] + b2[i])
    c3.append(a3[i] + b3[i])

  print(*c1, sep = '\n')
  print(*c2, sep = '\n')
  print(*c3, sep = '\n')
  # print(*(c1 + c2 + c3), sep='\n') # 1-line print statement
