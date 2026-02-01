# Declare these variables (x, y and z) as integers. Assign a value of 9 to x, Assign a value of 7 to y, perform addition, multiplication, division and subtraction on these two variables and Print out the result.
import math
x = 9
y = 7
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y) #remainder
print(x ** y) #x^y power operator
d = math.sqrt(25)
print(d)

# relational operators
print( x == y) #false
print(x != y) #true
print(x >= y)
print(x < y)

#assignment operators
num = 10
# num = num + 10 
num += 10 #for all operators
print(num)

#logical operators(not , and, or)
print(not (x > y) )
print(not False) #true

val1 = True
val2 = True
val3 = False
print("and operator", val1 and val2) #true
print("and operator: ", val1 and val3) #false
print("or operator", val1 or val2)
print("or operator", (x == y) or val3)