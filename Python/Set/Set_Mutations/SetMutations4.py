if__name__ == "__main__":
  _, A = int(input().strip(None)), set(map(int, input().split()))
  
  for i in range(int(input())):
      fun, _ = [i  for i in input().split(' ')]
      set_values = {*map(int, input().split(' '))}
      eval('A.' + fun + '(' + str(set_values) + ')')
  print(sum(A))
