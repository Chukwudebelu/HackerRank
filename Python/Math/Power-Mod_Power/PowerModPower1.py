# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
  a, b, m = map(eval, ["int(input())"]*3)
  print("%d\n%d" % (a**b, a**b % m))
