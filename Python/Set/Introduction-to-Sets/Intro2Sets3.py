def average(array):
    s = set(array)
    avg = sum(s)/len(s)
    return F'{avg:.3f}'
  
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
