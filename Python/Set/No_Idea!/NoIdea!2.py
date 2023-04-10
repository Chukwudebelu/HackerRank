# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    n, m = map(int, input().split(None))
    array_n = list(map(int, input().split()))
    A = set(int(_) for _ in input().split())
    B = set(int(_) for _ in input().split())
    
    happiness = 0
    for element in array_n:
        if element in A:
            happiness += 1
        elif element in B:
            happiness -= 1
        else:
            happiness += 0 # "continue" can also be used here
    print(happiness)
