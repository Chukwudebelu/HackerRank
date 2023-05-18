#!/bin/python3

if __name__ == "__main__":
  # Compute the 3 x 3 determinant of the system
  # Determinant = 0, when system of equations has *NO SOLUTIONS*
  det = lambda a: a*(2*a - 1) - 1*(a - 2) + 2*(1 - 4)
  
  # Hold all possible alpha values
  lst = list()
  
  # Loop through several values that make det = 0
  for i in range(-100, 101):
    if det(i) == 0:
      lst += [i]
      
  # Return the minimum value
  print(min(lst))
