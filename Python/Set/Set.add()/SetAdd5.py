if __name__ == "__main__":
  N = int(input())
  stamps = set()
  for _ in range(N):
    stamps.add(input())
  print(len(stamps))
