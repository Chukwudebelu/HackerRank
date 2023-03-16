def split_and_join(txt):
    return "-".join(txt.split(" "))
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
