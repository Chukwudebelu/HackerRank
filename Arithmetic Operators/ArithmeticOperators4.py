import operator

if __name__ == '__main__':
    a, b = map(int, [input(), input()])
    print(operator.add(a, b), operator.sub(a, b), operator.mul(a, b), sep = '\n')
