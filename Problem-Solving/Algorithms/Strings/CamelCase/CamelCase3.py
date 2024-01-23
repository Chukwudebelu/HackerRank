#!/bin/python3

if __name__ == '__main__':
    s: str = input().strip(None)
    i, num_of_words = 0, 1
    
    while (i < len(s)):
        if ('A' <= s[i] <= 'Z'):
            num_of_words += 1
        i += 1
    
    print(num_of_words)
