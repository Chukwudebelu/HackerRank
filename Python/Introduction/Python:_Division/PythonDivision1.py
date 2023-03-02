if __name__ == '__main__':
    a, b = [int(input()) for _ in range(2)]
    for op in ['//', '/']:
      print(eval(f'a{op}b'))
