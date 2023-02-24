if __name__ == "__main__":
  n, A, m, B = map(eval, ['input()', '{*map(int, input().split())}'] * 2)
  print(len(A & B))
