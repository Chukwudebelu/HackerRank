if __name__ == "__main__":
    M = int(input())
    setA = set(map(int, input().split()))
    
    N = int(input())
    setB =  set(map(int, input().split()))
    
    print(*sorted((setB.difference(setA))|(setA.difference(setB))), sep='\n')
