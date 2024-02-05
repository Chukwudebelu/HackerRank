#!/bin/python3

import os
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    meridien = s[-2:]
    s_hour_12 = s[:2]
    
    if meridien == 'AM': 
        s_hour_24 = '0' + str(int(s_hour_12.strip('0')) % 12) if s_hour_12 != '10' and s_hour_12 != '11' else str(int(s_hour_12) % 12)
        
    elif meridien == 'PM':
        s_hour_24 = str(int(s_hour_12.strip('0')) % 12 + 12) if s_hour_12 != '10' and s_hour_12 != '11' else str(int(s_hour_12) % 12 +12)
        
    return str(s_hour_24) + s[2:-2]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
