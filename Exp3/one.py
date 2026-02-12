#Find a factorial of given number.
a = int(input("Enter a nmber: "))
b = 1
for i in range(1, a+1):
    b = b * i
print("Factorial: ", b)

