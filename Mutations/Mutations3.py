def mutate_string(string, position, character):
    l, i = list(), 0
    while i < len(string):
      if (i == position):
        l += [character]
      else:
        l += [string[i]]
      i += 1
    return ''.join(l)
  
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
