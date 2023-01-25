# Complete the solve function below.
def solve(a):
  mod, P, i = 10**9 + 7, 1, 0
  while i < len(a):
    P *= (1 + pow(2, a[i], mod))
    i += 1
  P -= 1
  return P % mod
  
if __name__ == '__main__':
    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    print(result)
