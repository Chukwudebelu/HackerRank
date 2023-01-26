def hurdleRace(k, height):
    if max(height) > k:
      return max(height) - k
    else:
      return 0

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    print(result)
