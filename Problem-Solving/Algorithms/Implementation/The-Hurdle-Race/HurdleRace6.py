def hurdleRace(k, height):
    lst = []
    for i in height:
      if i > k:
        lst += [i-k]
    return max(lst) if len(lst) != 0 else 0

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    print(result)
