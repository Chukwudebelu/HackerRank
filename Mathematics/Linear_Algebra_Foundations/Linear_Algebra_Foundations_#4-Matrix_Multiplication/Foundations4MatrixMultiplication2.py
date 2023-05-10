# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    M = [[1, 2, 3], [2, 3, 4], [1, 1, 1]]
    N = [[4, 5, 6], [7, 8, 9], [4, 5, 7]]    
    P = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    for i in range(len(M)):
        for j in range(len(N[0])):
            for k in range(len(N)):
                P[i][j] += M[i][k] * N[k][j]
    for j in P:
        print(*j, sep='\n')
    
