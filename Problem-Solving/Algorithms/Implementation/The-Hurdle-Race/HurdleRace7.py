def hurdleRace(k, height):
    lst = []
    for i in height:
      if i > k:
        lst += [i-k]
    j = 1; n = len(lst)
    if n:
      max_ = lst[0];
      while j < n:
        if lst[j] > max_:
          max_ = lst[j]
        j += 1
      return max_
    else:
     return 0
  
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    print(result)
