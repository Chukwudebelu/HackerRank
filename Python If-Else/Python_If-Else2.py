if __name__ == '__main__':
    n = int(input().strip())
    
    x = 'Weird' if n % 2 == 1 else ('Not Weird' if 2 <= n <= 5 else('Weird' if 6 <= n <= 20 else 'Not Weird'))
    print(x)
