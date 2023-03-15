# No need to import 'textwrap' module/library

def wrap(string, max_width):
    s = ''; i = 0
    while i < len(string) + 1:
      s += string[i:i+max_width] + '\n'
      i += max_width
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
