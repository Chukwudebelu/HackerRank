def hurdleRace(k, height):
    height.sort(reverse=bool(1))
    return max(0, height[0]-k)
  
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    print(result)
