if __name__ == "__main__":
  n, A, m, B = ['input()', '{*map(int, input().split())}'] * 2
  eval(n); As = eval(A); eval(m); Bs = eval(B)
  print(len(As & Bs))
