def read_str() -> set[str]:
  i = input; i()
  return {*i().split()}
  
if __name__ == "__main__":
  print(len(read_str() | read_str()))
