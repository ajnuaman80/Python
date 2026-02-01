#Write a program which takes any date as input and display next date of the calendar 
#       e.g. 
#       I/P: day=20 month=9 year=2005 
#       O/P: day=21 month=9 year 2005
day = int(input("Enter the day:"))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):   
    leap = True
else:
    leap = False

if month in [4, 6, 9, 11]:
    days = 30
elif(month == 2):
    if(leap):
        days = 29
    else:
        days = 28
else:
    days = 31

if(day < days):
    day = day + 1  #day += 1
else:
    day = 1
    if(month == 12):    #if day = days then the month will change too
        month = 1
        year += 1
    else:
        month += 1

print("day =", day, "month =", month, "year =", year)
