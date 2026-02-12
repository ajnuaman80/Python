#Convert all lower cases to upper case in a string.
a = input("Enter a string: ")
b = ""

for c in a:
    if 'a' <= c <= 'z':
        b += chr(ord(c) - 32)
    else:
        b += c
print(b)
