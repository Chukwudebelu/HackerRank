cntr = '.|.'
delim = '-'
lst = []

def matf(n,m):
    for i in range(0,n//2):
        # Print top above WELCOME
        lst.append(((2*i + 1)*cntr).center(m, delim))
        
    text = 'WELCOME'
    lst.append(text.center(m,delim))

    for j in range(n//2 -1,-1,-1):
        # Print bettom below WELCOME
        lst.append(((2*j + 1)*cntr).center(m,delim))

    return '\n'.join(lst)

if __name__ == "__main__":
    n,m = list(map(int,input().split()))
    result = matf(n,m)
    print(result)
