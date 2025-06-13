#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re 

for _ in range(int(input())):
    UID = input('')
    
    if len(UID) != 10 or not re.match(r"[A-Za-z0-9]{10}" , UID):
        print("Invalid")
        continue
    
    if len(set(UID)) != len(list(UID)):
        print("Invalid")
        continue

    upper_alpha_count = 0
    num_count = 0
    for letter in UID:
        if letter.isalpha() and letter.isupper():
            upper_alpha_count += 1
        if letter.isdigit():
            num_count += 1

    if num_count < 3 or upper_alpha_count < 2:
        print("Invalid")     
    else:        
        print("Valid")
