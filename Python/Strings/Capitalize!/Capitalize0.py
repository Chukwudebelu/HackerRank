def solve(s):
    words = s.split(' ')
    return ' '.join([word.capitalize() for word in words])

if __name__ == '__main__':
    s = input()

    result = solve(s)

    print(result)
