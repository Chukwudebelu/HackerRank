if __name__ == '__main__':
  s: str = input()
  print(any(list(map(str.isalnum, s))))
  print(any(list(map(str.isalpha, s))))
  print(any(list(map(str.isdigit, s))))
  print(any(list(map(str.islower, s))))
  print(any(list(map(str.isupper, s))))
