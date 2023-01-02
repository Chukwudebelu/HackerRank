if __name__ == '__main__':
    a, b = map(int, [input(), input()])
    
    for operator in ['+', '-', '*']:
      print(eval(F'a{operator}b'))
