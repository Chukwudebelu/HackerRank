if __name__ == '__main__':
    N = int(input())
    records= [[input(),float(input())] for _ in range(N)]
    sort_ = lambda x: (-x[1],x[0])
    sort_records = sorted(records, key=sort_)
    remove_grade = sort_records[-1][1]
    sort_records = [rec for rec in sort_records if rec[1] != remove_grade]
    second_last = sort_records[-1][1]
    valid_lst = [valid[0] for valid in sort_records if valid[1] == second_last]
    print(*valid_lst, sep='\n')
