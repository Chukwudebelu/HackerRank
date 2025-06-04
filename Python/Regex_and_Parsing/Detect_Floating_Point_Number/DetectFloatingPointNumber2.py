#!/bin/Python3
# Without using Regex Module (Fails 3 Cases out of a Total of 18)

if __name__ == "__main__":
    T = int(input().strip(None))

    for _ in range(0, T):
        case = str(input(''))
        
        if case.isalnum() or case.isalpha() or case.isnumeric():
            print("False")
        else:
            start_sign = '+' == case[0] or '-' == case[0] or '.' == case[0]
            point_count = 0
            letter_check = 0
            
            for i in range(len(case)):
                if case[i] == '.':
                    point_count += 1
                if case[i].isalpha():
                    letter_check += 1
                    
            if (point_count == 1) and (letter_check == 0): # #.###
                print("True")
            elif start_sign and (point_count == 1) and (letter_check == 0): # +#.###
                print("True")
            else: 
                print("False")
