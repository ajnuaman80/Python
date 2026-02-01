# Write a program to compute the length of the hypotenuse (c) of a right triangle using Pythagoras theorem.
p = int(input("Enter the perpendicular of the triangle: "))
b = int(input("enter the base of thr triangle: "))
h = ( p*p + b*b)**(1/2)
print("Hypoteneus: ", h)