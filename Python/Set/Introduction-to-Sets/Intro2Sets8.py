import functools
from operator import add

def average(array):
  arr = set(array)
  return '{:.3f}'.format(functools.reduce(add, arr)/len(set(arr)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
