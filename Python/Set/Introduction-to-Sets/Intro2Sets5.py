def average(array):
    unique_array = set(array)
    avg = sum(unique_array)/len(unique_array)
    return '%.3f' % avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
