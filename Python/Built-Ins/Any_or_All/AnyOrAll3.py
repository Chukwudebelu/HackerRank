#!/bin/python3
# Solved without explicitly using list() or [] along with using string operations

def reversedStr2Int(x: str) -> str:
    return ''.join(reversed(x))
    
if __name__ == "__main__":
    input(); ll = input().split()
    positive = (y > '0' for y in ll)
    
    if all(positive):
        palindrome = (y == reversedStr2Int(y) for y in ll)
        print(positive and any(palindrome))
    else:
        print(False)
