if __name__ == "__main__":
    a = int(input().strip())
    b = int(input().strip())
    c = divmod(a, b)
    print(*c, c, sep='\n')
