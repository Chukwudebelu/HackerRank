# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

if __name__ == "__main__":
    K = int(input().strip()) 
    L = [int(_) for _ in input().split()]
        
    count = Counter(L)
    print(min(count, key = count.get))
