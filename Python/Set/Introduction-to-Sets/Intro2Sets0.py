def average(array):
    arr_dist = set(arr)
    n_dist = len(arr_dist)
    return sum(arr_dist)/n_dist

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
