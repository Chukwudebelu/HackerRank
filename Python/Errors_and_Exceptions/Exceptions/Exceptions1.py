#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
def error_exception(a, b) -> None:
    try:
        print(int(a) // int(b))
    except ZeroDivisionError as e1:
        print(F"Error Code: {e1}")
    except ValueError as e2:
        print(F"Error Code: {e2}")
    
if __name__ == "__main__":
    listA, listB = [[] for _ in range(2)]

    for k in range(int(input())):
        a, b = [str(_) for _ in input().split()]
        listA.append(a)
        listB.append(b)

        error_exception(listA[k], listB[k])
