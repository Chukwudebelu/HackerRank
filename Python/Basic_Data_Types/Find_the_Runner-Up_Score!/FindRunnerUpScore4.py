if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr); max_ = arr[0]
    i = 0
    while i < len(arr)-1:
      if max_ < arr[i+1]:
        max_ = arr[i+1]
      i += 1
    while max_ in arr:
      arr.remove(max_)
    print(max(arr))
