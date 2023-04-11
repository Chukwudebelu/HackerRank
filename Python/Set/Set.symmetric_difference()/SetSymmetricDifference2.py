# Enter your code here. Read input from STDIN. Print output to STDOUT
def len_symmetric_diff(A: set, B: set) -> int:
  return len((A - B) | (B - A))

  
if __name__ == "__main__":
  M, english = input(), set(input().split(" "))
  N, french = input(), set(input().split(" "))
  
  print(len_symmetric_diff(english, french))
