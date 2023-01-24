import itertools

def average(array):
  s = set(array)
  avg = (list(itertools.accumulate(s, lambda a,b: a+b))[-1])/len(s)
  return f'{avg:.3f}'

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
