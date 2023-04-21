# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == "__main__":
  A, B = [[*map(int, input().split(' '))] for _ in range(2)]
  print(*product(A, B))
