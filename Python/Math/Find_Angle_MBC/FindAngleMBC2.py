# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import degrees, atan

if __name__ == "__main__":
    AB = input().strip(None); BC = input().strip(None)
    angleMBC = round(degrees(atan(int(AB) / int(BC))))
    print('{0}\xb0'.format(angleMBC))
