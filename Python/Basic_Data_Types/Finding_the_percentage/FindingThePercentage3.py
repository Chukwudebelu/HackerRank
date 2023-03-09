if __name__ == '__main__':
    n = int(input())
    name_marks = dict()
    for _ in range(n):
      data = input().split(' ')
      name = data.pop(0)
      name_marks[name] = [*map(float, data)]
    name = input()  
    sum_ = 0
    for score in name_marks[name]:
      sum_ += score
    print("%.2f" % (sum_ / 3.0))
