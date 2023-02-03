if __name__ == "__main__":
  N = int(input())
  lst = [input() for _ in range(N)]
  unique_lst = []
  for j in lst:
     if j not in unique_lst:
      unique_lst += [j]
  print(len(unique_lst))
