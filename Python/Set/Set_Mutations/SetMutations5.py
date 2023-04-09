if __name__ == "__main__":
  input().lstrip(None).rstrip(None)
  a = {int(_) for _ in input().split(" ")}

  for _ in range(int(input().strip(None))):
      name, *_ = input().split()
      getattr(a, name)(set(map(int, input().split())))

  print(sum(a))
