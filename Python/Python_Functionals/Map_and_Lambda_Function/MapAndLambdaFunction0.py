#!/bin/python3
cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n: int) -> list:
    """  
    Return a list of fibonacci numbers
    """
    i = 0
    a, b = 0, 1
    lst = [a, b]
    while (i <= n-3):
        a, b = b, b + a
        lst.append(b)
        i += 1
    return lst[:n]

if __name__ == "__main__":
    n = int(input())
    print(list(map(cube, fibonacci(n))))
