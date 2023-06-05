#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == "__main__":
    N = int(input().strip())
    lowercase_letters = list(map(str, input().split()))
    K = int(input().strip())
    combo = list(combinations(lowercase_letters, K))
    combo_a = [i for i in combo if i.__contains__("a")]
    prob = len(combo_a)/len(combo)
    print(F'{prob:.3f}')
