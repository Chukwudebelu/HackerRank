if __name__ == "__main__":
  i = input
  n, A, m, B = map(eval, ['i()', '{*map(int, i().split())}'] * 2)
  print(len(A & B))
