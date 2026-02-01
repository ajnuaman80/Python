#Find the greatest among three numbers assuming no two values are same. 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if(a > b and a > c):
    print(a, "is the greatest")
elif(b > c and b > a):
    print(b, "is the greatest")
else:
    print(c, "is the greatest")