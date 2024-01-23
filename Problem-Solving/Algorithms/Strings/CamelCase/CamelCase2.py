#!/bin/python3

if __name__ == '__main__':    
    print([_ for _ in input().strip() if _ in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"].__len__() + 1)
