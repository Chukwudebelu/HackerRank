# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

if __name__ == "__main__":
  z = complex(input(""))
  r, phi = cmath.polar(z)
  print("%.3f\n%.3f" % (r, phi))
