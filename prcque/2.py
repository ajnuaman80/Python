#WAP to check if a list contains a palindrome of elements. Hint: use copy method
lis = [1, 2, 3, 4, 3, 2, 1]
lis2 = lis.copy()
lis2.reverse()
if(lis == lis2):
    print("Yes, the given list is a palindrome.")
else:
    print("Not palindrome")
