#Write a program to find if given number is prime number or not.
a = int(input("Enter a number: "))

if a <= 1:
    print("Not prime")
else:
    b = True
    for i in range(2, a):
        if a % i == 0:
            b = False
            break
    if b:
        print("Prime")
    else:
        print("Not prime")
