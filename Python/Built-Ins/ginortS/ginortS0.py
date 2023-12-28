# Enter your code here. Read input from STDIN. Print output to STDOUT
def ginortS(s):
  lst = list()
  lower = []; upper = []; odd = []; even = []
  
  for i in s:
    if 'a' <= i <= 'z':
      lower.append(i)
    elif 'A' <= i <= 'Z':
      upper.append(i)
    elif int(i) % 2:
      odd.append(i)
    elif not int(i) % 2:
      even.append(i)
      
  lower = sorted(lower)
  upper = sorted(upper)
  odd = sorted(odd)
  even = sorted(even)
  
  lst.extend([*lower, *upper, *odd, *even])
  return ''.join(lst)
      

if __name__ == "__main__":
  S = input()
  print(ginortS(S))
