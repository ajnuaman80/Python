#Write a program to print the following pattern
# 123454321
# 1234 *4321
# 123  * * 321
# 12   * * *  21
# 1    * * * *   1
n = 5
for i in range(n):
    for j in range(1, n - i + 1): #for left digits
        print(j, end="")

    print(" " * i, end="") #for spaces

    if i > 0:
        print("* " * i, end="")  #for stars

    print(" " * i, end="")  #spaces after star

    for j in range(n - i, 0, -1):  #for right digits
        print(j, end="")

    print() #for nect line

