def closestNumber(a, b, x):
    if a == 1:
      return 1
    elif b == 0:
      return 0
    else:
      lesser = int(a**b - (a**b % x))
      greater = a**b + int(x - (a**b % x))
      dless, dgreater = a**b - lesser, greater - a**b
      return lesser if dless < dgreater else greater
