if __name__ == "__main__":
  n = int(input().strip())
  print(hash(tuple([int(i) for i in input().split()])))
