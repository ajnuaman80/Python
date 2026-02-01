#  Write a program to print truth table for bitwise operators (&, | and ^ operators) 
print("A B   A&B A|B A^B")
for a in range(2):
    for b in range(2):
        print(a, b, "| ", a & b, "|", a | b, "|", a ^ b)
