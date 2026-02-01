# Write a program to swap two numbers without taking additional variable.
a = 5
b = 8
print(a, b)
a, b = b, a #Python ka built-in feature tuple unpacking
print("After swapping: ", a, b)


# Tuple unpacking means assigning values of a tuple to multiple variables at the same time, where each variable receives the corresponding value from the tuple.i