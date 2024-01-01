#!/bin/python3

if __name__ == "__main__":
  sort_string = input()
  lower_case, upper_case, even_case, odd_case = [], [], [], []
  for i in sort_string:
      if str(i).islower():
          lower_case.append(i)
      elif str(i).isupper():
          upper_case.append(i)
      elif str(i).isnumeric():
          if int(i) % 2 == 0:
              even_case.append(i)
          else:
              odd_case.append(i)
      
  lower = "".join(sorted(lower_case))
  upper = "".join(sorted(upper_case))
  even = "".join(sorted(even_case))
  odd = "".join(sorted(odd_case))
  print(f"{lower}{upper}{odd}{even}")
