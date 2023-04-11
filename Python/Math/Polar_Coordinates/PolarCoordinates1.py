# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase

if __name__ == "__main__":
  comp = complex(input())
  print('{r}\n{a}'.format(r = abs(comp), a = phase(comp)))
