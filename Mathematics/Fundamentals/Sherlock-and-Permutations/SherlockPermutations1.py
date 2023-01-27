def solve(n, m):
  mod = 1000000007
  return math.comb(n + m - 1, m - 1) % mod

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = solve(n, m)
    
        print(result)
