from itertools import accumulate
from operator import add

def average(array):
    s = list(set(array))
    return round(list(accumulate(s, add))[-1]/len(s),3)
  
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
