# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

def permute_upper(S, k):
    lst = []
    for i in list(permutations(sorted(S), int(k))):
      lst.append(''.join(list(i)))

    return lst
            
if __name__ == "__main__":
    S, k = input().split()
    result = permute_upper(S, int(k))
    for k in result:
        print(k)
