if __name__ == "__main__":
  A = {*map(int, input().split())}
  N = int(input().strip())
  lst = [set(map(int,input().split())).issubset(A) for _ in range(N)]
  print(all(lst))
