import functools

def average(array):
  arr = set(array)
  return round(functools.reduce(lambda a,b: a+b, arr)/len(set(arr)), 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
