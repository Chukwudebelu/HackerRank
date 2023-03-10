if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
# lst = arr.split()
lst = list(arr)
num_max = max(lst)

for i in range(len(lst)):
    if num_max in lst:
        lst.remove(num_max)
    
print(max(lst)) # runner-up is the max after the original max is dropped
