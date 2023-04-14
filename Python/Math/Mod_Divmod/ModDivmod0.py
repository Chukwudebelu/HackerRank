# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    a, b = int(input().strip()), int(input().strip())
    print(F'{a // b}\n{a % b}\n({a // b}, {a % b})')
