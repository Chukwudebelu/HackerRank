#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
def error_exception(a, b):
    try:
        print(int(a) // int(b))
    except ZeroDivisionError as e1:
        print("Error Code:", e1)
    except ValueError as e2:
        print("Error Code:", e2)
    
if __name__ == "__main__":
    T = int(input())
    lst_a = []
    lst_b = []
    for _ in range(T):
        a, b = map(str, input().split())
        lst_a += [a]
        lst_b += [b]

        error_exception(lst_a[_], lst_b[_])
