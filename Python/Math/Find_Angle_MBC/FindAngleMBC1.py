# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import *

if __name__ == "__main__":
    AB, BC = int(input().strip()), int(input().strip())
    angleMBC = round(degrees(atan(AB / BC)))
    print("%g%s" % (angleMBC, '\xb0'))
