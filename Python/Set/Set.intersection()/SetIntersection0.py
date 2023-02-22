if __name__ == "__main__":
    n = int(input().strip())
    setA = set(map(int, input().split()))
    b = int(input().strip())
    setB = set(map(int, input().split()))
    print(len(setA.intersection(setB)))
