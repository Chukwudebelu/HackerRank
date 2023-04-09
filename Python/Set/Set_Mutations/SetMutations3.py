if __name__ == "__main__":
    N = int(input().strip(None))
    A = set(int(i) for i in input().split(" "))
    set_ops = {'update': A.update, 
               'intersection_update': A.intersection_update, 
               'symmetric_difference_update' : A.symmetric_difference_update, 
               'difference_update': A.difference_update}
    for i in range(int(input().strip())):
        set_ops[input().split()[0]]({int(i) for i in input().split()})

    print(sum(A))
