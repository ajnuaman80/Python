#Check whether the quadratic equation has real roots or imaginary roots. Display the roots
import math

print("Basic quadratic equation: ax^2 + bx + c = 0")
a = float(input("Enter the coefficient of x^2 i.e. 'a': "))
b = float(input("Enter the coefficient of x i.e.e 'b': "))
c = float(input("Enter the constant i.e. 'c': "))

d = (b**2) - 4*a*c   #discriminant

if(d > 0):
    print("Real and distinct roots")
    m = (-b + math.sqrt(d)) / (2*a)
    n = (-b - math.sqrt(d)) / (2*a)
    print("Roots are: ", m, n)
elif(d == 0):
    print("Real and equal roots")
    m = -b  / (2*a)
    print("Roots are: ", m, m)
else:         #i.e. d=negative
    print("Imaginary roots")
    print("Form: (real part) + (imaginary part)i")
    m = int(-b  / (2*a))   #real part
    n = int((math.sqrt(-d)) / 2*a)     #took -ve sign to neutralize the -ve d value
    print("Roots are: ", m, "+", n,"i", "and", m, "-", n,"i")



