#!/bin/python3

if __name__ == '__main__':
    s = input(None).lstrip().rstrip()
    count = 1
    for char in s:
        if char.isupper():
            count += 1
    print(count)
