#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

def ginortS(s: str) -> str:
  """
  Sort the input string according to the given constraints:
  1st group: LOWERCASE characters
  2nd group: UPPERCASE characters
  3rd group: ODD integers
  4th group: EVEN integers
  """
  lower, upper, odd, even = [list() for _ in range(4)]
  
  for i in s:
    if 'a' <= i <= 'z':
      lower.append(i)
    elif 'A' <= i <= 'Z':
      upper.append(i)
    elif int(i) % 2:
      odd.append(i)
    else:
      even.append(i)
    
  lower, upper, odd, even = map(sorted, [lower, upper, odd, even])
  
  return ''.join([*lower, *upper, *odd, *even])
      

if __name__ == "__main__":
  print(ginortS(input()))
