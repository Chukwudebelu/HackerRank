def closestNumber(a, b, x):
    if a**b == 1:
      return a if a == 1 else b
    else:
      lesser = int(a**b - (a**b % x))
      greater = a**b + int(x - (a**b % x))
      dless, dgreater = a**b - lesser, greater - a**b
      return lesser if dless < dgreater else greater
