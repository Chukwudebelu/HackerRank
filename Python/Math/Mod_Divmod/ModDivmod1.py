# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":   
    a, b = (input().strip() for _ in range(2))
    a, b = int(a[:]), int(b[:])
    print('{0}\n{1}\n{2}'.format(a // b, a % b, divmod(a, b)))
