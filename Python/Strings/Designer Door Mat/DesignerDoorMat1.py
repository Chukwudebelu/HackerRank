if __name__ == "__main__":
    n,m = map(int,input().split())

    #top
    for i in range(1,n,2):
        print((i*".|.").center(m,"-"))
        
    # center
    print("WELCOME".center(m,"-"))
        
    # bottom
    for i in range(n-2,0,-2):
        print((i*".|.").center(m,"-"))
