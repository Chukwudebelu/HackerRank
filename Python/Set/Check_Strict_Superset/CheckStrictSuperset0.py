# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    A = {int(_) for _ in input().split()}
    n = int(input().strip())
    lst = []
    for _ in range(n):
        B = set(map(int, input().split()))
        lst.append(B)
               
    print(all(1 if A.issuperset(i) and A != i else 0 for i in lst))
