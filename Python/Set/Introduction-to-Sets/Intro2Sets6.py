def average(array):
    sum_ = 0; count = 0
    for _ in range(len(array)):
      if array[:_+1].count(array[_]) == 1:
        sum_ += array[_]
        count += 1
    return round(sum_/count, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
