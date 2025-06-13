#!/bin/python3
# Without using the Regex Module
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    T = int(input().rstrip().lstrip())
    
    all_uids = []
    for _ in range(T):
        all_uids += [input().strip()]
        
    lst = []
    for uid in all_uids:
        check_length = True
        check_alnum = True
        check_unique = True
        
        if len(uid) != 10:
            check_length = False
            
        count_up = 0; count_num = 0
        for char in uid:
            if char.isalpha() and char.isupper():
                count_up += 1
            elif char.isdigit():
                count_num += 1
        
        if count_up < 2 or count_num < 3:
            check_alnum = False

        if len(uid) != len(set(uid)):
            check_unique = False
            
        lst += ['Valid' if check_length and check_alnum and check_unique else 'Invalid']
    
    print(*lst, sep = '\n')
