#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

def polynomial(x: int, k: int) -> int:
    """
    Compute: P(x) = 1 + x + x^2 + x^3 + ... + x^(k-1)
    """
    a: int = 0
    for i in range(k):
        a += x**(i)
    return a
    
    
if __name__ == "__main__":
    x, k = input().strip().split(" ", 2)
    func_eval = polynomial(int(x), int(k))
    print(True) if (func_eval == int(k)) else print(False)
