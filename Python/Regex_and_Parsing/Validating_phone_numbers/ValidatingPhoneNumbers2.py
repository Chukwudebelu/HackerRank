#!/bin/python3
# Without using the Regex Module
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    N = int(input('').rstrip().lstrip())
  
    lst = []
    for _ in range(N):
        s = input()
        lst += [s]
    
    for number in lst:
        if number.__len__() != 10:
            print('NO')
        elif bool(number.isnumeric()) is False:
            print('NO')
        else:
            print('YES'*(number[0] in ['7', '8', '9']) + 'NO'*(not number[0] in ['7', '8', '9']))
