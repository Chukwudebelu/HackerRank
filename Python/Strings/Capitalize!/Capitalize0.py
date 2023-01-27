if __name__ == "__main__":
  S = str(input())
  words = S.split(' ')
  print(' '.join([word.capitalize() for word in words]))
