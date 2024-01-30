#!/bin/python3
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr: list) -> None:
    n = len(arr)
    count_pos = count_neg = count_zero = 0
    
    for i in range(n):
        if arr[i] > 0:
            count_pos += 1
        elif arr[i] < 0:
            count_neg += 1
        else:
            count_zero += 1
        
    # Calculate the ratios of positive, negative, and zero elements
    ratio_pos = count_pos/n
    ratio_neg = count_neg/n
    ratio_zero = count_zero/n
    
    print(F'{ratio_pos:.6f}\n{ratio_neg:.6f}\n{ratio_zero:.6f}')

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().lstrip().rstrip().split()))
    plusMinus(arr)
