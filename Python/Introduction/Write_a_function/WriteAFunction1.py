def is_leap(year):
    leap = False
    
    if year % 400 == 0:
        return not leap
    elif year % 4 == 0:
        return leap if year % 100 == 0 else not leap
    return leap

if __name__ == "__main__":
  year = int(input())
  print(is_leap(year))
