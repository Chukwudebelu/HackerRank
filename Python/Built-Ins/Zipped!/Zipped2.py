#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    '''
    Without using the Built-in/predefined "zip()" function
    '''
    N, X = map(int, input().split(" "))
    scores = [0.0 for _ in range(N)]
    for i in range(X):
        subject_scores = [float(_) for _ in input().split()]
        for s in range(N):
            scores[s] += subject_scores[s]
            
    print(*map(lambda S: S / X, scores), sep='\n')
