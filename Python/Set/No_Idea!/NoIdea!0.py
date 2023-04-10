# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
  n, m = list(int(_) for _ in input().split(" "))
  lst = [*map(int, input().split())]
  A, B = set(), set()
  for i in input().split():
    A.add(int(i))
  for j in input().split():
    B.add(int(j))
    
  happiness = 0
  for num in lst:
    if num in A:
      happiness += 1
    elif num in B:
      happiness -= 1
    else:
      continue
  print(happiness)
    
