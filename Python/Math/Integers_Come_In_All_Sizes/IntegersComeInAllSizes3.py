# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
  a, b, c, d = map(int, [input() for _ in range(4)])
  print(a**b + c**d)
