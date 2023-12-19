#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    i = input
    N, X = [int(_) for _ in i().split()]
    zipped = zip(*[map(float, i().split()) for _ in range(X)])
    [print(sum(scores)/X) for scores in zipped]
