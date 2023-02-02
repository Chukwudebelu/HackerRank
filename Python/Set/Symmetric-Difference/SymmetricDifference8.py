if __name__ == "__main__":
  _, a = input(), set(map(int, input().split()))
  _, b = input(), set(map(int, input().split()))
  print(*sorted(a ^ b), sep="\n")
