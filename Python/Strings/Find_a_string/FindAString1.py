def count_substring(string: str, sub_string: str) -> int:
  m, n = len(sub_string), len(string)
  return len([i for i in range(n-m+1) if string[i:i+m] == sub_string])

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
