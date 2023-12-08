#!/bin/python3

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

if __name__ == "__main__":
    month, day, year = list(map(str, input().split()))
    
    # cal = calendar.TextCalendar(firstweekday=6).formatyear(int(year))
    # day = date_input[1]
    # year = date_input[2]

    print(calendar.day_name[calendar.weekday(int(year), int(month), int(day))].upper())
