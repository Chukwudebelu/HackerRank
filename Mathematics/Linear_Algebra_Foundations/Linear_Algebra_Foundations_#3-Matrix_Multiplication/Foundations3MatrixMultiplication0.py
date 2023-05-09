if __name__ == "__main__":
    M, N = [[1, 2], [2, 3]], [[4, 5], [7, 8]]
    
    lst = []
    for row1m in M:
        for j in range(len(row1m)-1):
            lst += [row1m[j]*N[0][0] + row1m[j+1]*N[1][0]]
            lst += [row1m[j]*N[0][1] + row1m[j+1]*N[1][1]]  
    print(*lst, sep='\n')
