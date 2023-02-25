# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
  i = input
  _, A, _, B = [i(), [*map(int, i().split())], i(), [*map(int, i().split())]]
  C = list()
  for elem in A:
    if not (elem in B):
      C.append(elem)
  print(len(C))
