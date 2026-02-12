#Write a program to print sum of digits
a = int(input("Enter a number: "))

sum = 0
while a > 0:
    b = a % 10
    sum = sum + b
    a = a // 10

print(sum)
