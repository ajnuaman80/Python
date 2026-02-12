#Check whether given number is palindrome or not.
a = int(input("Enter a number: "))
b = a
rev = 0

while b > 0:
    c = b % 10
    rev = rev * 10 + c
    b //= 10

if(rev == a):
    print("Palindrome")
else:
    print("Not Palindrome")
