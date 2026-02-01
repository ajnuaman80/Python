# Write a program to find left shift and right shift values of a given number.
a = int(input("Enter a number: "))
shift = int(input("Enter number of shifts: "))
leftShift = a << shift  #<< Left Shift, bits ko left shirft krega -> multiply by 2ⁿ
rightShift = a >> shift # >> Right Shift, bits ko right shift krega -> divide by 2ⁿ
print("Real number:", a)
print("Left shift: ", leftShift)
print("Right shift: ", rightShift)
