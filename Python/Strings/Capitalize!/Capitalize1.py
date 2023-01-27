def solve(s):
    for word in s.split():
        s = s.replace(word, word.capitalize())
    return s

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result
