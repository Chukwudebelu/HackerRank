# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    n, setA = int(input().rstrip()), set(map(int, input().split()))
    b, setB = int(input().rstrip()), set(map(int, input().split()))
    
    print(len(setA - setB))
