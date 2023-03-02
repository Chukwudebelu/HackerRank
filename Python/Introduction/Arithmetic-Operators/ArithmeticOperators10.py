class ArithmeticOperator(object):
  def __init__(self, a, b):
    self.a = a
    self.b = b
    
  def addition(self):
    return self.a + self.b
  
  def subtraction(self):
    return self.a - self.b
  
  def multiplication(self):
    return self.a * self.b
  
    
if __name__ == '__main__':
    a, b = map(int, [input(), input()])
    num = ArithmeticOperator(a, b);
    print(num.addition())
    print(num.subtraction())
    print(num.multiplication())
