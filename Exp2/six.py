 #Find whether a given year is a leap year or not
year = int(input("Enter the year: "))

if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):   #1 year = 365.2422 days. so used this logic for best outcome
    print("Leap year")
else:
    print("Not a leap year")


