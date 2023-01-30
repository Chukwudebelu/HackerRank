def maximumDraws(n):
    return round(n*(1 + 1/n), None)
  
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = maximumDraws(n)

        print(result)
