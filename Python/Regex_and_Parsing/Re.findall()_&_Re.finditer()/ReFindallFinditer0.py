#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == "__main__":
    S = input()
    pattern = r'(?<=[BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz])([aeiouAEIOU]{2,})(?=[BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz])'
    matches = re.findall(pattern, S)
  
    if matches:
        for match in matches:
            print(match)
    else:
        print(-1)
