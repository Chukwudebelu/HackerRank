if __name__ == "__main__":
    M = int(input())
    setA = set(map(int, input().split()))
    
    N = int(input())
    setB =  set(map(int, input().split()))
    
    print(*sorted((setA.difference(setB)).union(setB.difference(setA))), sep='\n')
