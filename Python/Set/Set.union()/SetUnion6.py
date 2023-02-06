if __name__ == "__main__":
  i = input; 
  _, A = i(), [*map(int, i().split())]
  _, B = i(), [*map(int, i().split())]
  count = len(A)
  for elem in B:
    if elem not in A:
      count += 1
  print(count)
