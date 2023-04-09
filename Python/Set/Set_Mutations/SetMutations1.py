def set_mutate(op, n, A, B):
    if op == "intersection_update":
        A.intersection_update(B)
    elif op == "update":
        A.update(B)
    elif op == "symmetric_difference_update":
        A.symmetric_difference_update(B)
    elif op == "difference_update":
        A.difference_update(B)
    return A
        
if __name__ == "__main__":
    _ = int(input().strip(None))
    A = set(int(x) for x in input().split())
    n = int(input().strip(None))
    
    for _ in range(n):
        op, m = input().split()
        m = int(m.strip(None))
        B = {*map(int, input().split())}
        set_mutate(op, m, A, B)
    print(sum(A))
