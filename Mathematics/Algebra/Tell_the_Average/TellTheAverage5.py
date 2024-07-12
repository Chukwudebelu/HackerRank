# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
sys.setrecursionlimit(10**6)  # Max size of L: 10^6 (i.e. 1,000,000)

def value_of_S_recursive2(L: list) -> int:    
    if (len(L) == 0):    # empty list: L = []
        return 0
    elif (len(L) == 1):  # unary list: L = [a]
        return L[0]
    else:           # other lists: L = [a, b, ...]
        a, b = L[:2]    # a, b = [L[0], L[1]]
        L.pop(1)
        L[0] = ((a + 1)*(b + 1) - 1) % (1000000007)  # a + b + ab = (a + 1)(b + 1) -1
        return value_of_S_recursive2(L)


if __name__ == "__main__":
    input()
    _List_ = []
    
    for l in input('').split(" "):
        _List_.append(int(l))
        
    print(value_of_S_recursive2(_List_))
