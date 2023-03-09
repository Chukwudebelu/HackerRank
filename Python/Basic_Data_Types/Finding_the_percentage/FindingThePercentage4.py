if __name__ == '__main__':
    n = int(input())
    name_marks = dict()
    for _ in range(n):
      data = input().split(' ')
      name_marks[data[0]] = [float(i) for i in data[1:]]
    query_name = input()
    avg_score = sum(name_marks[query_name]) / 3
    print(f'{avg_score:.2f}')
