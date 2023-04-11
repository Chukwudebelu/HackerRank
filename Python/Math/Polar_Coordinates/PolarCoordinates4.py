# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

def main():
  # Read complex # from STDIN
  z = complex(input())
  
  # Modulus of complex #, z
  r = abs(z)
  
  # Phase of complex #, z
  phi = cmath.phase(z)
  
  # Round to 3 decimal places
  print(F'{r:.3f}\n{phi:.3f}')


if __name__ == "__main__":
  main()
