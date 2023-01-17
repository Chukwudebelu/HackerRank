if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_sort = list(set(arr))
    arr_sort.sort(reverse=True)
    print(arr_sort[1])
