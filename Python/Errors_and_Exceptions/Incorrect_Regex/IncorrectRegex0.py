#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
    
import re
    
if __name__ == "__main__":
    T = int(input())
    
    for i in range(T):
        try:
            reg = re.compile(input())
            print(True)
        except re.error:
            print(False)    
