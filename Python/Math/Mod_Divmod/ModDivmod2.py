if __name__ == "__main__":
    a, b = map(int, [input().strip(), input().strip()])
    print('{0}\n{1}\n({0}, {1})'.format(a // b, a % b))
