from operator import add, sub, mul

if __name__ == '__main__':
    a, b = map(int, [input() for _ in range(2)])
    print(F'{a+b}\n{a-b}\n{a*b}')
