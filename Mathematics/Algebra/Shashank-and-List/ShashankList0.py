import functools

def solve(a):
  mod = 1000000007
  xp2 = lambda x: 1 + pow(2, x, mod)
  P = functools.reduce(lambda a, b: a * b, list(map(xp2, a)))
  return (P - 1) % mod

if __name__ == '__main__':
    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    print(result)
