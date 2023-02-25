# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
  i = input
  _, A, _, B = [i(), [*map(int, i().split())], i(), [*map(int, i().split())]]
  print(len([elem for elem in A if elem not in B]))
