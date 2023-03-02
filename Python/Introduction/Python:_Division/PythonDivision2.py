import operator

if __name__ == '__main__':
    a, b = (int(input()) for _ in range(2))
    print(operator.floordiv(a, b), operator.truediv(a, b), sep='\n')
