#!/bin/python3
def solve(a):
  m = 10**9 + 7
  result = 1

  for i in range(len(a)):
      result *= (1+pow(2, a[i], m))
  result -= 1

  return int(result % m)

if __name__ == '__main__':
    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    print(result)
