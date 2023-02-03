def distinctCountry(arr):
    print(len(arr))
    
if __name__ == "__main__":
    s = int(input())
    lst = set()
    for _ in range(s):
        lst.add(input().strip())
        
    distinctCountry(lst)
