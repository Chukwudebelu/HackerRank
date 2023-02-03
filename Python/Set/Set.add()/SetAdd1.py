if __name__ == "__main__":
    N = int(input().strip())
    i = 0
    countries = set()
    while i < N:
        s = input()
        countries.add(s)
        i += 1
    print(len(countries))
