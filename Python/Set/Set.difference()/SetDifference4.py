if __name__ == "__main__":
  _, A = input(), list(*map(int, input().split()))
  _, B = input(), list(*map(int, input().split()))
  count = 0
  for elem in A:
    if elem not in B:
      count += 1
  print(count)
