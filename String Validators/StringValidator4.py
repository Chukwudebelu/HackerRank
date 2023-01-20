if __name__ == '__main__':
    s = input()
    for method in 'isalnum','isalpha','isdigit','islower','isupper':
      print(any(map(lambda x: getattr(x, method)(), s)))
