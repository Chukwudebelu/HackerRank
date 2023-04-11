# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import polar

if __name__ == "__main__":
  print(*polar(complex(input())), sep = "\n")
