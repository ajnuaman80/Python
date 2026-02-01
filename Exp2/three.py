#Find the greatest among the two numbers. If numbers are equal than print “numbers are equal”.
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if(a > b):
    print(a, "is greater than", b)
elif(a == b):
    print(a, "and", b, "are equal.")
else:
    print(b, "is greater than", a)