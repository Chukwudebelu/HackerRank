#!/bin/python3

import math as m
import os
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER p
#

def checkperfectsquare(n: int) -> bool:
 r = m.sqrt(n)
 if (int(r)**2 == n):
   return True
 else: 
   return False

def solve(D: int, P: int):
 if (D < 0):
   return 0
 if (D == 0):
  if (P < 0): return 0
  if (P == 0): return 1 # the pair (0, 0) is the only solution
  if (P > 0):
   if checkperfectsquare(P):
     return 2
   # The pairs (sqrt(P), sqrt(P)) and (-sqrt(P), -sqrt(P)) are the only solutions
   else:
     return 0
 if (D > 0):
  if (P == 0): return 4
  # The solutions are the pairs (D, 0), (0, D), (-D, 0), and (0, -D)
  else:
   discriminant = D**2 + 4*P
   if (discriminant < 0): return 0 # no real solutions
   elif (discriminant == 0):
    if (D % 2 == 0): return 2 # solutions are (D/2,-D/2) and (-D/2,D/2)
    else: return 0
   else:
    if not(checkperfectsquare(discriminant)): return 0
    else:
     rootdisc = int(m.sqrt(discriminant))
     if ((D + rootdisc) % 2 == 0):
      A = (D + rootdisc) // 2
      if (P % A == 0): return 4
      # Solutions are (A,B), (B,A), (-A,-B), and (-B,-A) such that A = (D + rootdisc)//2 and B = (-D + rootdisc)//2
      else: return 0
     else: return 0
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        d = int(first_multiple_input[0])

        p = int(first_multiple_input[1])

        result = solve(d, p)

        fptr.write(str(result) + '\n')

    fptr.close()
