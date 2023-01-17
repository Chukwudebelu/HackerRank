def split_and_join(string):
  new_string = ''
  for char in string:
    if char == ' ':
      new_string += '-'
    else:
      new_string += char
  return new_string
  
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
