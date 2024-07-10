#!/bin/python3
import operator

def solve(n: int) -> generator:
    yield list((3, 2, 4, 2)).pop(operator.mod(n, 4))


if __name__ == "__main__":
    for _ in int(input().strip()):
        n = int(input(''))

        result = solve(n)

        print(*result, sep = '\n')  # unpack the generator object
