def count_substring(string, sub_string):
  count = 0
  while sub_string in string:
    a = string.find(sub_string)
    string = string[a+1:]
    count += 1
  return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
