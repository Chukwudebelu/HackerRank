#!/bin/python3
import math

class Complex(object):
  def __init__(self, real, imaginary):
    self.real = round(real, 2)
    self.imaginary = round(imaginary, 2)
        
  def __add__(self, no):
    add_real = self.real + no.real
    add_imag = self.imaginary + no.imaginary
    add_sgn = '+' if (add_imag) >= 0 else ''
    return f'{add_real:.2f}' + add_sgn + f'{add_imag:.2f}i'
        
  def __sub__(self, no):
    sub_real = self.real - no.real
    sub_imag = self.imaginary - no.imaginary
    sub_sgn = '+' if (sub_imag) >= 0 else '' 
    return f'{sub_real:.2f}' + sub_sgn + f'{sub_imag:.2f}i'
        
  def __mul__(self, no):
    a, b = self.real, self.imaginary
    c, d = no.real, no.imaginary
    mul_real = a*c - b*d
    mul_imag = a*d + b*c
    mul_sgn = '+' if (mul_imag) >= 0 else ''
    return f'{mul_real:.2f}' + mul_sgn + f'{mul_imag:.2f}i'

  def __truediv__(self, no):
    a, b = self.real, self.imaginary
    c, d = no.real, no.imaginary
    div_real = (a*c + b*d)/(c**2 + d**2)
    div_imag = (b*c - a*d)/(c**2 + d**2)
    div_sgn = '+' if (div_imag) >= 0 else str()
    return f'{div_real:.2f}' + div_sgn + f'{div_imag:.2f}i'

  def mod(self):
    return '{0:.2f}+0.00i'.format(math.sqrt(self.real**2 + self.imaginary**2))

  def __str__(self):
    if self.imaginary == 0:
      result = "%.2f+0.00i" % (self.real)
    elif self.real == 0:
      if self.imaginary >= 0:
        result = "0.00+%.2fi" % (self.imaginary)
      else:
        result = "0.00-%.2fi" % (abs(self.imaginary))
    elif self.imaginary > 0:
      result = "%.2f+%.2fi" % (self.real, self.imaginary)
    else:
      result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
    return result

if __name__ == '__main__':
  c = map(float, input().split())
  d = map(float, input().split())
  x = Complex(*c)
  y = Complex(*d)
  print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
