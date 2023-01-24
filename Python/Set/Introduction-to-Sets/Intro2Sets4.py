def average(array):
    return '{0:.3f}'.format(sum(set(array))/len(set(array)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
