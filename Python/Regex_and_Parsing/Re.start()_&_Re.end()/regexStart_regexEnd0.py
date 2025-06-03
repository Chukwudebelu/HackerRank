#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == "__main__":
    S = input().strip(None)
    k = input().strip(None)
    
    indexes = []
    
    for _ in range(0, len(S)):
        m = re.search(r'' + k, S[_:])

        if m is not None:
            index = (m.start() + _, m.end() + _ - 1)
            
            if index not in indexes:  # Get rid of duplicates
                indexes += [index]
  
    print(*indexes, sep = '\n') if len(indexes) else print('(-1, -1)')
