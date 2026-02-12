#Find whether the given number is Armstrong number.
a = int(input("Enter a number: "))
b = a
d = len(str(a))
sum = 0

while b > 0:
    e = b % 10
    sum += e ** d
    b //= 10

if(sum == a):
    print("Yes")
else:
    print("Nope")
