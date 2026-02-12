x = 9
y = 7
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y) #remainder
print(x ** y) #x^y power operator

# relational operators
print( x == y) #false
print(x != y) #true
print(x >= y)
print(x < y)

#assignment operators
num = 10
# num = num + 10 
num += 10 #for all operators
print(num)

#logical operators(not , and, or)
print(not (x > y) )
print(not False) #true

val1 = True
val2 = True
val3 = False
print("and operator", val1 and val2) #true
print("and operator: ", val1 and val3) #false
print("or operator", val1 or val2)
print("or operator", (x == y) or val3)

#type conversion
a = 2
b = 6.25
sum = a + b
print(sum) #2.0 + 6.25

#type casting
c = "3"
d = int(c) # or c = int("3")
print(d + b)
e = str(b)
print(type(e))

#input in python

name = input("Enter your name: ")
print("Welcome ", name)  #input is always a string data type

num = input("Enter your age: ")
print(type(num))

gf = int(input("How many gf ? : "))
print(type(gf), gf)

a =2 #a is an integer
b = 5
c = "Winter" # c is a string
d = 5.26 #d is a floating point number
f = False # boolean variable
print("I am Aman.", "I am a boy")
print("sum : ", a + d + b)
print(type(b))
print(type(c))
x = None
print(x)
print(type(x))
j = a + b
print(j)

#String and conditional statements !!!!!!!!     

str1 = "Hello World, \tthis is a string \nwe are creating in python."
str2 = 'World'
str3 = """I am AJ"""
print(str1)
#concatination
print(str2+str3)
final_str= str1 + "" + str2 + str3
print(len(str1))
len1 = len(str1)
len3= len(final_str)

#Indexing
str = "Apna_college" #str[0] is A str[1] is p
print(str[3])
#str[4]= "a" not allowed

#Slicing
# accessing parts of a string
# str[starting index : ending index] ending index not included
print(str[1 : 4])
print(str[1 : len(str)])
print(str[: 4]) #[0:4]
print(str[1 : ]) #[1: len(str)]


#Slicing negative index
str = "i am Winter and i am a coder"
#backward counting
print(str[-3:-1]) #pl

print(str.endswith("er"))  # returns true if the string ends with er
print(str.capitalize())  #string k initial ko capital kr dega ek baar. no changes to original string
print(str)   # yaha changes cancel ho jayenge
str = str.capitalize()  #but yaha humne original string ko modify kr diya h
print(str.replace("coder", "poet")) #ye replace krdega temporary. agar permanent krna h to upar ki tarah kro
print(str)
print(str.find("o")) # o k word k index number retrurn dega
print(str.count("am")) # am kitni baar exist krta hvo btaega


# if-elif-else (SYNTAX)
age = 18
if(age > 18):
    print("Eligible")    #indentation- spacing proper
elif(age == 18):
    print("barely")
else:
    print("not eligible")

# Lists and Tuples
marks = [45.4, 76, 88, 29, 66.4]   #List
print(marks[4])
print(len(marks))
marks[4] = 69

list = ["Aman", 19, "Haryana"] #list is mutable
print(list)

#list slicing is possible
print(marks[:4]) #4 not included

#str = "Hello" #string is immutable

print(marks[-3:-1])

#list methods
list.append("student") #add one element at the end . also called mutating
print(list)

marks.sort() #assending mein sort hogi
print(marks)
marks.sort( reverse=True)
print(marks)

list.reverse() #list ko reverse krega
print(list)

list.insert(3, "Poet") #add poet to inddex 3
print(list)

marks.remove(76) #76 ki first occurance ko delete krega
list.pop(3) #3rd index ko delete krega

#Tuples
#A built in data type that lets us create immutable sequence of values

#immutable
list = [2, 3, 4, 6, 78] 

tup = (2, 1, 3, 1, 67, 55, 19, 18)
print(tup[3])

tupp = ()
print(type(tupp))

tu = (1) #yaha python samjhega apne bass ek integer liye h
print(type(tu)) #thats why comma lagana important h

print(tup[1:3])
print(tup.index(19)) #this will give us the index of the first occurence of the integer 19 in the tupple 
print(tup.count(1)) #thiss will give us the count of 1 in the tupple

#Dictionaries and Sets
# used to store data values in key : values pairs
 #onordered, mutuable and don't allow duplicate keys

dic = {
    "name" : "Aman",
    "age" : 19,
    "learning" : "coding",
    "subjects" : ["python", "C", "C++", "HTML", "CSS"],
    "topics" : ("Dictonaries", "Sets"),
    "is_adult" : True,
    12.99 : 94.99
}

print(type(dic))
print(dic["topics"]) #to access any value through key
dic["learning"] = "Subjects"
print(dic)

null_dic = {}  #null dictonary
print(null_dic)
null_dic["name"] = "AJ"

#Nesting in dictonaries
student = {
    "name" : "AJ",
    "subjects" : {
        "phy" : 97,
        "che" : 93,
        "math" : 99
    }
}

print(student["subjects"]["phy"])  #to acces the elements inside the dictionaryu of a dictionary

print(student.keys()) # returns the keys of the dicyonary
print(list(student.keys())) # type casting in lists
print(len(list(student.keys()))) #returns no of keys
print(student.values()) #returns the values of the dictonary
  
