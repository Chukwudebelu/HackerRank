# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    print(sum([pow(int(input()), int(input())) for _ in range(2)]))
