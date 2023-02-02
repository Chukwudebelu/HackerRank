if __name__ == "__main__":
  _, a = input(), set(input().split())
  _, b = input(), set(input().split())
  for x in sorted([int(x) for x in a.symmetric_difference(b)]):
      print(x)
