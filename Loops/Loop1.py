if __name__ == '__main__':
    n = int(input())
    print(*[i ** 2 for i in range(n)], sep='\n')
