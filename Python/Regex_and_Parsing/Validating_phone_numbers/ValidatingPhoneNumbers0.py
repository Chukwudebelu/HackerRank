#!/bin/python3
# Without using the Regex Module
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    N = int(input('').strip())
    lst = []
    
    for _ in range(N):
        s = input()
        lst.append(s)

    for number in lst:
        if len(number) != 10:
            print('NO')
        elif not number.isdigit():
            print('NO')
        else:
            if number.startswith('7') or number.startswith('8') or number.startswith('9'):
                print('YES')
            else:
                print('NO')
