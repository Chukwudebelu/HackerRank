if __name__ == "__main__":
    M = int(input()); A = set(map(int, input().split()))
    N = int(input()); B = set(map(int, input().split()))
    print(*sorted((B - A).union((A - B))), sep='\n')
