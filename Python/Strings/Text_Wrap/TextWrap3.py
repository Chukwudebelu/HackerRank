def wrap(string, max_width):
    for i in range(1, len(string) // max_width + 1):
        string = string[:i*max_width+i-1] + '\n' + string[i*max_width+i-1:]
    return string
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
