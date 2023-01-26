def closestNumber(a, b, x):
    aEb = a**b
    if aEb == 1:
      return a if a == 1 else b
    else:
      lesser = int(aEb - (aEb % x))
      greater = aEb + int(x - (aEb % x))
      dless, dgreater = aEb - lesser, greater - aEb
      return lesser if dless < dgreater else greater
