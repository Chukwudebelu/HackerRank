#!/bin/python3
#
# Complete the 'solve' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts INTEGER_ARRAY balls as parameter.
#

def solve(balls) -> str:    
    return str(sum(balls) * 0.5)


if __name__ == '__main__':
    N, all_ball_numbers = int(input('').strip(None)), list()
    
    for _ in range(0, N, 1):
        ball_num = int(input().strip())
        all_ball_numbers += [ball_num]

    print(solve(all_ball_numbers).format("%.1f"))
