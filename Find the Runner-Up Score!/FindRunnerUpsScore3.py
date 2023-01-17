if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_ = max(arr)
    print(max([j for j in arr if j != max_]))
