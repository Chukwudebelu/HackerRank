def count_substring(string, sub_string):
  i, count = string.find(sub_string), 0
  if i == -1:
    return count
  else:
    count = 0;
    while i < len(string) - len(sub_string) + 1:
      if string[i:i+len(sub_string)] == sub_string:
        count += 1
      i += 1
    return count
  
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
