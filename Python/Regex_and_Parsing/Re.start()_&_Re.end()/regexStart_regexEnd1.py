#!/bin/python3
# Without using the Regex Module

if __name__ == "__main__":
    S, k = [input('')] * 2
    
    for i in range(len(S)):
        if S[i:i+len(k)] == k: # Check if substrings in S match k
            print((i,i+len(k)-1))
            
    if k not in S:
        print((-1,-1))
