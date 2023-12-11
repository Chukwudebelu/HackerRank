#!/bin/python3
import os
from datetime import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):
  fmt = "%a %d %b %Y %H:%M:%S %z"
  t1, t2 = [dt.strptime(i, fmt) for i in [t1, t2]]
  return f'{abs(int((t1-t2).total_seconds()))}'

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  t = int(input())

  for t_itr in range(t):
      t1 = input()

      t2 = input()

      delta = time_delta(t1, t2)

      fptr.write(delta + '\n')

  fptr.close()
