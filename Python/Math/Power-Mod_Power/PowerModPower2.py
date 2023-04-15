# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if __name__ == "__main__":
  a, b, m = map(int, sys.stdin)
  print(F'{pow(a,b)}\n{pow(a,b,m)}')
