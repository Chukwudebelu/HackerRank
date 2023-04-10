if __name__ == "__main__":
  _, arr = int(input()), input()
  A = set(input().split())
  B = set(input().split())
  print(sum((a in A) - (a in B) for a in arr.split()))
