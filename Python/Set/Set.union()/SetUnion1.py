def union_all(A, B):
    A_set = set(A)
    B_set = set(B)
    return len(A_set.union(B_set))

if __name__ == "__main__":
    num_eng_paper = int(input())
    
    eng_paper = list(map(int, input().split()))

    num_fre_paper = int(input())

    fre_paper = list(map(int, input().split()))
    
    result = union_all(eng_paper, fre_paper)
    print(result)
