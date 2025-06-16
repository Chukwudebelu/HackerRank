#!/bin/python3
# Fails some parts of "Test Case 3"!
# Enter your code here. Read input from STDIN. Print output to STDOUTz
import re


if __name__ == "__main__":
    pattern1 = r"^[a-zA-Z0-9]{10}$"    # Exactly 10 alphanumeric characters in a valid UID
    pattern2 = r"(?=.*[A-Z]){2,}"    # Contain at least 2 uppercase alphabet characters
    pattern3 = r"(?=.*[0-9]){3,}"    # Contain at least 3 digits
    pattern4 = r"(?!.*(.).*\1.*)"    # No character repeats
    
    T = int(input().strip())
    
    for _ in range(0, T):
        UID: str = input('')
        
        cond1 = re.match(pattern1, UID)
        cond2 = re.match(pattern2, UID)
        cond3 = re.match(pattern3, UID)
        cond4 = re.match(pattern4, UID)
        
        print("Valid" if all([cond1, cond2, cond3, cond4]) else "Invalid")
