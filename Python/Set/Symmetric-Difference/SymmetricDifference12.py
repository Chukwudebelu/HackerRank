if __name__ == "__main__":
  i = input; I = int
  M = I(i()); A = [*map(I, i().split())]
  N = I(i()); B = [*map(I, i().split())]
  lst = list()
  for i in range(M):
    if A[i] in B:
      continue
    else:
      if A[i] not in lst:
        lst += [A[i]]
  for j in range(N):
    if B[j] in A:
      continue
    else:
      if B[j] not in lst:
        lst += [B[j]]
  lst.sort()
  print(*lst, sep = "\n")
