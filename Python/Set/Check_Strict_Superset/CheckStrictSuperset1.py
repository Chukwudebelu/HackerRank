if __name__ == "__main__":
  A = {*map(int, input().split())}
  N = int(input().strip())
  lst = [set(map(int,input().split())) for _ in range(N)]
   
  count = 0 # count the number of times a set in lst is a proper subset
  while count < N:
    if A.issuperset(lst[count]) is True: # and A != B
      count += 1
      continue
    else:
      break
    
  print(True if count == N else False)
