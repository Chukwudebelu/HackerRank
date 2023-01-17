def split_and_join(string):
  new_string = ''
  for char in string:
    new_string += '-' if char == ' ' else char
  return new_string
      
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
