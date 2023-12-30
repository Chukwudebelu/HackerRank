#!/bin/python3

if __name__ == "__main__":
  S = input()
  S = sorted(list(S))
  lowercase_, uppercase_, even_digits, odd_digits = [], [], [], []
  for s in S:
      if s.islower():
          lowercase_.append(s)
      elif s.isupper():
          uppercase_.append(s)
      elif s.isdigit():
          if int(s) % 2 == 0:
              even_digits.append(s)
          else:
              odd_digits.append(s)
  print(''.join(lowercase_ + uppercase_ + odd_digits + even_digits))
