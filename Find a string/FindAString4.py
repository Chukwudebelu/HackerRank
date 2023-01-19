def count_substring(string, sub_string):
  occurs = 0
  while string.__contains__(sub_string):
    if string.find(sub_string) != -1:
      string = string[string.find(sub_string)+1:]
      occurs += 1
  return occurs
  

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
