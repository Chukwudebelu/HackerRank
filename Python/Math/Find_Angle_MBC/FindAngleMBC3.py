# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

if __name__ == "__main__":
  AB, BC = [int(input('').strip()) for _ in range(2)]
  print(str(round(math.degrees(math.atan(AB / BC)))) + "\xb0")
