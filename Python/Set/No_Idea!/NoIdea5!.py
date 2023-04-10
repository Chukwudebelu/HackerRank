# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
  n, m = map(int, input().split(" "))
  lst = input().split(" ")
  A, B = [{*input().split()} for _ in range(2)]
  
  sign = lambda x, A, B: 1 if x in A else (-1 if x in B else 0)
  happiness = 0
  for i in range(n):
    happiness += sign(lst[i],A,B)
  print(happiness)
  
  
