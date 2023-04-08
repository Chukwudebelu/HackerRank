# Enter your code here. Read input from STDIN. Print output to STDOUT

def set_mutate(op, n, A, B):
    if op == "intersection_update":
       A &= B # A.intersection_update(B)
    elif op == "update":
       A |= B # A.update(B)
    elif op == "symmetric_difference_update":
        A ^= B # A.symmetric_difference_update(B)
    elif op == "difference_update":
        A -= B # A.difference_update(B)
    return A
        
if __name__ == "__main__":
    _ = int(input().strip(None))
    A = {int(x) for x in input().split(" ")}
    n = int(input().strip())
    
    for _ in range(n):
        l = input().split()
        op = l[0]
        m = int(l[1].strip())
        B = set(map(int, input().split()))
        set_mutate(op, m, A, B)
    print(sum(A))
