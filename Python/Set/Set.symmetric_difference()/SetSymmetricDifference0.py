# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    m, setA = int(input().strip()), {int(i) for i in input().split()}
    n, setB = int(input().strip()), {int(j) for j in input().split()}
    
    print(len(setA ^ setB))
