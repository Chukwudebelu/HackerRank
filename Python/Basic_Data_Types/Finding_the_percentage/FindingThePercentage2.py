if __name__ == '__main__':
    n = int(input())
    name_marks = dict()
    for _ in range(n):
      data = input().split(' ')
      name_marks[data[0]] = sum(map(float, data[1:])) / 3.0
    name = input()        
    print('{0:.2f}'.format(name_marks[name]))
      
