def split_and_join(txt):
    return txt.replace(" ", "-")
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
