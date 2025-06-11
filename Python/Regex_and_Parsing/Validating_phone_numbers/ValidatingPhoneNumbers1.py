#!/bin/python3
# Without using the Regex Module
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    N = int(input().strip(None))
  
    llst = [input('') for _ in range(N)]
    
    for num in lst:
        if len(num) != 10:
            print('NO')
        elif num.isnumeric() == 0:
            print('NO')
        else:
            print('YES' if any([num.startswith('7'), num.startswith('8'), num.startswith('9')]) else 'NO')
