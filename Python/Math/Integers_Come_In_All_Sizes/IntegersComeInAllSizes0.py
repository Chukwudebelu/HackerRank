# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    a, b, c, d = [int(input().strip(None)) for _ in range(4)]
    print(a**b + c**d)
