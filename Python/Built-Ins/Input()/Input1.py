#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    x, k = [int(_) for _ in input().split(' ')]

    function_evaluation = eval(input())
    print(function_evaluation == k)
