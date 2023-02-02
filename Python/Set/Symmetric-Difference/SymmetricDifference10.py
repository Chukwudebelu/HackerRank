if __name__ == "__main__":
  _, A = input(), set(map(int, input().split()))
  _, B = input(), set(map(int, input().split()))
  print(*sorted((A.union(B)).difference(A.intersection(B))), sep="\n")
