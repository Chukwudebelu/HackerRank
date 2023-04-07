from collections import Counter

if __name__ == "__main__":
  K = int(input().strip(None))
  rooms = list(map(int, input().split()))
  room_cap = [x for x, y in (Counter(rooms)).items() if y != K]
  print(*room_cap)
