#!/bin/python3
def plusMinus(arr: list) -> None:
    elem = [0, 0, 0]
    total = len(arr)
    
    for num in arr:
        if (num > 0):
            elem[0] += 1  # positive elements
        elif (num < 0):
            elem[1] += 1  # negative elements
        else:
            elem[2] += 1  # zero elements
        
    print(*[round(elem[i]/total, 6) for i in [0, 1, 2]], sep='\n')

if __name__ == '__main__':
    int(input().strip())
    plusMinus([int(_) for _ in input().split()])
