def swap_case(s):
    stg = ''
    for i in range(len(s)):
        if s[i].isupper():
            stg += s[i].lower()
        elif s[i].islower():
            stg += s[i].upper()
        else:
            stg += s[i]
    return stg

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
