# Write a program to convert given seconds into hours, minutes and remaining seconds.
x = int(input("Enter seconds: "))
h = int(x / 3600)
a = int(x % 3600)
m = int(a / 60)
s = int(a % 60)
print(h,"hours", m, "minutes", s, "seconds")
