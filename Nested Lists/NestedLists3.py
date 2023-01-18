if __name__ == '__main__':
    N = int(input())
    records= [[input(),float(input())] for _ in range(N)]
    lst = [rec for rec in records if rec[1]!=min([char[1] for char in records])]
    lst2 = [valid[0] for valid in lst if valid[1]==min([i[1] for i in lst])]
    print(*sorted(lst2),sep='\n')
