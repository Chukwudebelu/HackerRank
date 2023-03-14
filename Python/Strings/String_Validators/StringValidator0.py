if __name__ == '__main__':
    s = input()
    itert = range(len(s))
    for i in itert:
        if s[i].isalnum():
            print(s[i].isalnum())
            break
    else:
        print(False)
            
    for i in itert:
        if s[i].isalpha():
            print(s[i].isalpha())
            break
    else:
        print(False)
            
    for i in itert:
        if s[i].isdigit():
            print(s[i].isdigit())
            break
    else:
        print(False)
            
    for i in itert:
        if s[i].islower():
            print(s[i].islower())
            break
    else:
        print(False)
            
    for i in itert:
        if s[i].isupper():
            print(s[i].isupper())
            break
    else:
        print(False)
