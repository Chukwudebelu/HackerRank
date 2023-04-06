if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        n, A = int(input().strip()), set(map(int, input().split()))
        m, B = int(input().strip()), set(map(int, input().split()))
        
        print(True if A == B&A else False)
