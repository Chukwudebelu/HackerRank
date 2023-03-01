from operator import add, sub, mul

if __name__ == '__main__':
    a, b = [int(input().strip()) for _ in range(2)]
    
    for op in ['add', 'sub', 'mul']:
      print(eval(f'{op}(a, b)'))
