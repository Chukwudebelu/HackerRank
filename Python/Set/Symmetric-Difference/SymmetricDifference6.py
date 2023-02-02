if __name__ == "__main__":
    M = int(input()); A = set(map(int, input().split()))
    N = int(input()); B = set(map(int, input().split()))
    print(*sorted((A - B).union(B.difference(A))), sep='\n')
    
