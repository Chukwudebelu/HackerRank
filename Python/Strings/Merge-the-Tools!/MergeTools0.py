def merge_the_tools(string, k):
    n = len(string)
    lst = [string[j*k : (j+1)*k] for j in range(n//k)]

    for j in lst:
      print(''.join(dict.fromkeys(j)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
