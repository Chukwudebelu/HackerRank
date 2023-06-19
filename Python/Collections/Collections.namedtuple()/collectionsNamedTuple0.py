#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

if __name__ == "__main__":
    N = int(input()) # Total number of students
    column_names = list(map(str, input().upper().split())) # Names of columns
    student_list = namedtuple('student', column_names)

    lst = []
    for _ in range(N):
        lst.append(student_list(*list(map(str, input().split()))))
        
    sum_marks = 0
    for i in range(len(lst)):
        sum_marks += int(lst[i].MARKS)
            
    print('%.2f' % (sum_marks / N))
