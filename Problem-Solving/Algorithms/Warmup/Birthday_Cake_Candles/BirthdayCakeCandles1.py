#!/bin/python3
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles: list) -> int:
    candles = sorted(candles, reverse=0)
    max_h = 0

    for candle in candles:
        if (candle >= max_h):
            max_h = candle
    return len([_ for _ in candles if (_ == max_h)])

if __name__ == '__main__':
    input()
    print(birthdayCakeCandles([*map(int, input().split(' '))]))
