#!/bin/python3
#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def solve_steps(N: int) -> str:       
    return F'Go On Bob {int((pow(8*N + 1, 1/2) - 1)/2)}' if ((pow(8*N + 1, 1/2) - 1) % 2 == 0) else "Better Luck Next Time"


if __name__ == "__main__":
    T = int(input('').strip())
  
    [print(solve_steps(int(input().lstrip().rstrip()))) for t in range(0, T)]
