# Enter your code here. Read input from STDIN. Print output to STDOUT
from functools import reduce

if __name__ == "__main__":
  n = int(input().strip(None))
  A = {*map(int, input().split(" "))}
  N = int(input().lstrip(None).rstrip(None))
  
  for _ in range(N):
    set_details = input().split()
    
    set_operation = set_details[0]
    
    set_length = int(set_details[1])
    
    B = set(int(_) for _ in input().split(" "))
    
    getattr(A, set_operation)(B)
  
  """
  Return the sum of elements in non-empty set A
  If A is the empty set (i.e. {}), display 0.
  """
  print(reduce(lambda a, b: a + b, [*A]) if A else 0)
