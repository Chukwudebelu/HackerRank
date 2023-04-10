# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
  n, m = input().split(" ")
  lst = input().split()
  A, B = [{*input().split()} for _ in range(2)]
  
  happiness = 0
  for i in lst:
    happiness += int(i in A) - int(i in B)
  print(happiness)
