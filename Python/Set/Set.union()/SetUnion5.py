if __name__ == "__main__":
  i = input; 
  _, A = i(), [*map(int, i().split())]
  _, B = i(), [*map(int, i().split())]
  C = list(A)
  for elem in B:
    if elem in A:
      continue
    else:
      C += [elem]
  print(len(C))
