def is_leap(year):
    leap = False
    
    #Written Code:
    
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

year = int(input())