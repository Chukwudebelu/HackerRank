# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import atan2, pi

if __name__ == "__main__":
  AB, BC = int(input()), int(input())
  theta = (atan2(AB, BC) / pi) * 180 # Convert radians to degrees
  print(F'{theta:.0f}\N{DEGREE SIGN}')
