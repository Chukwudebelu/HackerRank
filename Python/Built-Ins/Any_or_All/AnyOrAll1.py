#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

def isPalindromic(x: int) -> bool:
    original_num = x
    reverse = 0
    while x:
        digit = x % 10
        reverse = reverse*10 + digit
        x //= 10
    return (original_num == reverse)
    
    
if __name__ == "__main__":
    _ = int(input())
    lst = list(map(int, input().strip().split(' ')))
    all_positive = all([*map(lambda x: x > 0, lst)])
    any_palindrome = any(list(map(isPalindromic, lst)))
    print(all_positive and any_palindrome)
