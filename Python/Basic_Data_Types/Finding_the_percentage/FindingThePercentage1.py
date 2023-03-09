if __name__ == '__main__':
    n = int(input())
    name_marks = []
    for _ in range(n):
      name, *marks = input().split(' ')
      name_marks += [(name,[*map(float,marks)])]
    query_name = input()
    
    for student in name_marks:
      if query_name == student[0]:
        avg_score = sum(student[1]) / len(student[1])
        
    print(F'{avg_score:.2f}')
