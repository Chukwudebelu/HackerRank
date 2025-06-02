#!/bin/python3
#
# Complete the 'solve' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts INTEGER_ARRAY balls as parameter.
#

def solve(balls) -> float:
    S: int = 0   # Sum of the numbers written on each ball
    
    for i in range(len(balls)):
        ball_num = balls[i]
        S += ball_num
        
    EX = S / 2
    
    return round(EX, 1)  # Round to 1 decimal place
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    balls_count = int(input().strip())

    balls = []

    for _ in range(balls_count):
        balls_item = int(input().strip())
        balls.append(balls_item)

    result = solve(balls)

    fptr.write(str(result) + '\n')
    fptr.close()
