def solve(n, m):
    return math.comb(n + m - 1, n) % (10**9 + 7)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = solve(n, m)

        print(result)
