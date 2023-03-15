# No need to import 'textwrap' module/library
def wrap(string, max_width):
    lst = []; i = 0
    while i < len(string) + 1:
      lst += [string[i:i+max_width]]
      i += max_width
    return '\n'.join(lst)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
