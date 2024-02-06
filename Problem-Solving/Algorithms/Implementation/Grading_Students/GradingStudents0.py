#!/bin/python3

import os
#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    final_grade = []
    for i in grades:
        rem = 5 - (i % 5)
        
        if (i >= 38):
            if (rem < 3):
                num = i + rem
                final_grade.append(str(num))
            elif (rem == 3):
                final_grade.append(str(i))
            else:
                final_grade.append(str(i))
        else:
            final_grade.append(str(i))
    return final_grade

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
