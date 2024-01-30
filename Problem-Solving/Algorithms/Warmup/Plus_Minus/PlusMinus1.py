#!/bin/python3

if __name__ == "__main__":
    input(); arr = [*map(int, input().split(" "))]
    
    vals, n = list(), len(arr)
    vals += [len([num for num in arr if num > 0])] # positive values
    vals += [len([num for num in arr if num < 0])] # negative values
    vals += [len([num for num in arr if num == 0])] # zero values
    
    print(*[F'{val/n:.6f}' for val in vals], sep = '\n')
