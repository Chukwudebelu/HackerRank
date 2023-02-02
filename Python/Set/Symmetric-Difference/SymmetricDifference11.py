if __name__ == "__main__":
  i = input;
  r = lambda: {*map(int, i().split())};
  i();
  m = r();
  i();
  print(*sorted(m ^ r()), sep="\n")
