# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

if __name__ == "__main__":
  z = complex(input(''))
  real_z, imag_z = z.real, z.imag
  
  r = pow(real_z**2 + imag_z**2, 0.5)
  phi = math.atan2(imag_z, real_z)
  print("{0}\n{1}".format(r, phi))
