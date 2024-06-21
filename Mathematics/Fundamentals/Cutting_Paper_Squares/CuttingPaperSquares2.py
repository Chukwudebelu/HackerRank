#!/bin/python3

import operator

# Without using the "solve" function

if __name__ == "__main__":
    _ = [int(_) for _ in input().strip().split(None)]
    print(operator.add(operator.mul(_[0], _[1]), -1))
