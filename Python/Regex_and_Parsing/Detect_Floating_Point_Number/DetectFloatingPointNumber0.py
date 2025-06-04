#!/bin/python3
import re

def check(n) -> None:
    for i in n:
        try:
            x = re.search(r"^[-+]?[0-9]*\.[0-9]+$", i)
            print(bool(x))
        except:
            print("False")


if __name__ == "__main__":
    T = int(input().rstrip())
    N = [str(input()) for _ in range(T)]
    check(N)
