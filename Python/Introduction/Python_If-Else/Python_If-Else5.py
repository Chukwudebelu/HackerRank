if __name__ == '__main__':
    n = int(input().strip())
    print('Weird'*(n % 2 or (n % 2 == 0 and 6 <= n <= 20)) + 'Not Weird'*(n % 2 == 0 and (n > 20 or 2 <= n <= 5)))
