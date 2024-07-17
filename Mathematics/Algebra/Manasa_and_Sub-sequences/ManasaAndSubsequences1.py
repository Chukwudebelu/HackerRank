#!/bin/python3
#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def powMod(m: int, n: int) -> int:
    MODULO = 10**9 + 7
    return pow(m, n, MODULO)
    
def solve(S: str) -> int:
    n = len(S)  # number of digits in sequence
    T: int = 0  # total number of candies
    
    for k in range(0, n):
        T += (powMod(2, k) * powMod(11, n-1-k) * powMod(int(S[k]), 1))
    return powMod(T, 1)
    

if __name__ == "__main__":
    S = input()
    print(solve(S), end = '\n')
