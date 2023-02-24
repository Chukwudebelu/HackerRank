# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
  i = input
  _, A, _, B = map(eval, ['i()', '[*map(int, i().split())]']*2)
  count = 0
  for elem in A:
    if elem in B:
      count += 1
  print(count)
