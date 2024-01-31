#!/bin/python3

def staircase(n):
    # Write your code here
    return [' '*(n-i) + '#'*i for i in range(1, n+1)]
        
if __name__ == '__main__':
    print(*staircase(int(input())), sep='\n')
