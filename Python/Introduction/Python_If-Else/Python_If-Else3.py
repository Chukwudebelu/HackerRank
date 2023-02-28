if __name__ == '__main__':
    n = int(input().strip())
    cond1 = 'Weird' if 6 <= n <= 20 else 'Not Weird'
    cond2 = 'Not Weird' if 2 <= n <= 5 else(cond1)
    cond3 = 'Weird' if n % 2 == 1 else (cond2)
    print(cond3)
