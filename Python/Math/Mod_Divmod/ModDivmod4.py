if __name__ == "__main__":
  divModAB: tuple = divmod(*map(int, [input(), input()]))
  print(*divModAB, divModAB, sep = "\n")
