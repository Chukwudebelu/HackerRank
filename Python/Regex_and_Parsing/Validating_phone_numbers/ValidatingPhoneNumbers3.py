#!/bin/python3
# Without using the Regex Module
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    N = int(input().strip())
    lst = list(input('') for i in range(N))
    [print('NO' if len(n) != 10 else ('NO' if not n.isdigit() else ('YES' if any([n[0] == '7', n[0] == '8', n[0] == '9']) else 'NO'))) for n in lst]
