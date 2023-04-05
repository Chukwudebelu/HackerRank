def main():
  A = set([int(a) for a in input().split()])
  N = int(input())
  lst = list()
  for _ in range(N):
    lst += [{*map(int,input().split())}]
  count = 0
  C = map(A.issuperset, lst)
  print(all(C))    

  
if __name__ == "__main__":
  main()
