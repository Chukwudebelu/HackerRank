from operator import add, sub, mul

if __name__ == '__main__':
    a, b = map(int, [input() for _ in range(2)])
    print('{0}\n{1}\n{2}'.format(a+b, a-b, a*b))
