# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
sys.setrecursionlimit(10**6)

def value_of_S_recursive3(L: list) -> int:
    if (L.__len__() == 0):
        return list()
    elif (L.__len__() == 1):  # unary list: L = [a]
        return L[0]
    else:           # other lists: L = [a, b, ...]
        a = L[0]; b = L[1];
        L = L[:1] + L[2:]    # leave out L[1] using list slicing
        L[0] = (a + b + a*b) % (1_000_000_000 + 7)
        return value_of_S_recursive3(L)
        
if __name__ == "__main__":
    int(input())
    print(value_of_S_recursive3([int(_) for _ in input('').split(' ')]))
