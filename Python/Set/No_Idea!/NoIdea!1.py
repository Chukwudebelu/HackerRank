# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    n, m = map(int, input().split())
    array_n = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    
    happiness = 0
    
    for i in array_n:
        happiness += (1 if i in A else (-1 if i in B else 0))
    print(happiness)
