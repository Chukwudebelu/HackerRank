#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple as ndtl

if __name__ == "__main__":
  N = int(input()) # Total # of students
  student_list = ndtl('student', input().split()) # Namedtuple of column names
  print(sum([int(student_list(*input().split()).MARKS) for _ in range(N)]) / N)
