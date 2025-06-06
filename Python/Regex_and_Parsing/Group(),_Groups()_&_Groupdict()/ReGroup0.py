#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

if __name__ == "__main__":
    S = input().strip()
    m = re.search(r'([a-zA-Z0-9])\1{1,}', S)
    print(m.group()[0] if m else -1)
