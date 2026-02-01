#Check whether the given number is divisible by 3 and 5 both
n = int(input("Enter a number: "))
if(n % 3 == 0 and n % 5 == 0):
    print("Yes")
else:
    print("Nope")