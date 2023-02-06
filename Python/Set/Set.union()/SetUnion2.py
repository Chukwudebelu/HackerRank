if __name__ == "__main__":
  _, A = int(input()), set(input().split())
  _, B = int(input()), set(input().split())
  print(len(A | B))
