def main() -> None:
  """
  For two given sets, A and B
  Determine if A is a subset of B
  """
  # Number of test cases
  T = int(input().strip())
  _ = 0
  while _ < T:
    n, A, m, B = [int(input().strip()), set([int(k) for k in input().split(' ')]), int(input().strip()),set([int(k) for k in input().split(' ')])]
    print(A.issubset(B))
    _ += 1
    
    
if __name__ == "__main__":
  main()
