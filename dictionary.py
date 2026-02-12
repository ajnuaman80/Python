# Dictionary. . .
# A mutable, unordered, collection of key-value pairs
# Key-value pair ---> Data stored as key : value
# Unordered ----> No indexing like lists (conceptually: stored by hashing)

student = {
    "name" : "Aman",       # key : value
    "age" : 19,        # key ---> used to acces data
    "course" : "CSE"   # value ---> actual data stored
}
print(student)

# Creating Dictionaries
d1 = { "a" : 1, "b" : 2}    # Using {}

d2 = dict(name = "Aman", age = 19)    # Using dict() function

d3 = {}      # empty dictionary, not set
print(type(d3))
print(d1, d2, d3)

# Dictionary Properties
#    Keys must be unique
d4 = { "a" : 1, "a" : 2}
print(d4["a"])          # Later values overwrite earlier ones
#    Keys must be immutable (hashable)
#    Allowed keys : int, float, string, tuple (with immutable elements)
#    Not allowed : list, set, dictionary
#                  for eg. d = {[1, 2] : "A"}  ---> Error
#                                              dictionary uses hashing --> keys must be hashable

# Accessing Values 
#  using key
print(student["name"])         # shows error if key is missing
#  using get()
print(student.get("age"))      # no error even if key is missing

print("---------------------------------")

# Adding and Updating Elements
# student = {
#     "name" : "Aman",       # key : value
#     "age" : 19,        # key ---> used to acces data
#     "course" : "CSE"   # value ---> actual data stored
# }
student["batch"] = 16    # adds new key-value pair
student["course"] = "CSE AIML"    # update existing value
print(student)

print("-------------------------------")

# Removing Elements
fruits = {
    'apple': 1,
    'banana': 2,
    'cherry': 3,
    'date': 4
}
fruits.pop("banana")
print(fruits)

fruits.popitem()   # removes last inserted key-value pair
print(fruits)

del fruits["cherry"]
print(fruits)

fruits.clear()
print(fruits)

print("--------------------------------")

# Dictionary Methods
print(student.keys())    # all keys
print(student.values())  # all values
print(student.items())   # key-value pairs as tuples 

print("--------------------------------")

# Looping through dictionary
for key in student:
    print(key)

print(" - - -")

for value in student.values():
    print(value)

print(" - - -")

for key, value in student.items():
    print(key, value)

print("--------------------------------")
#------------------------------------------------------------------------------------------------------
#   Tuple Unpacking
# Tuple unpacking means assigning multiple values from a tuple into multiple variables in a single line.
# for example
# t = (10, 20)

# a,b = t 
# print(a)  #10
# print(b)  #20

# Here a gets 10 and b gets 20
# python automatically splits the tuple

# Now, tuples in dictionary
# when you use: d.items()
# it returns tuples
# for example:  
d = {"name" : "Aman", "age" : 19}
print(d.items())      # each element is a tuple
#                       (key, value)

# How Unpacking Happens in Dictionary Loop
# Without Unpacking
for item in d.items():
    print(item)
# ('name', 'Aman')
# ('age', 19)
# Here item is a tuple
print(" - - -")
# With Tuple Unpacking
for key, value in d.items():
    print(key, value)
# Now what happens
# Python automatically does this internally:
# (key, value) = ('name', 'Aman')
# (key, value) = ('age', 19)
# So, key gets first element of the tuple
#     value gets second element 
# this is tuple unpacking

# Unpacking in Nested dictionaries
record = {
    "Aman" : {"math" : 90, "cs" : 95},
    "Aniket" : {"math" : 12, "cs" : -1}     
 }
for name, marks in record.items():       # name gets outer key and marks get inner dictionary
    print(name, marks)

print(" - - - ")
for name, marks in record.items():    # deeper unpacking
    for subject, score in marks.items():
        print(name, subject, score)


# Why helpful ? -----> cleaner and more readable

#------------------------------------------------------------------------------------------------------
print("----------------------------------------------------")

# Nested Dictionaries
hello = {
    "name" : "Aman",
    "marks" : {
        "math" : 90,
        "cs" : 96
    }
}
print(hello["marks"]["cs"])
# student["marks"]  --> inner dictionary
# ["cs"] --> value

print("----------------------------------------------------")

# Dictionary Comprehension
squares = {x: x*x for x in range(1,6)}
#         key  value     loop
# for every x, python creates key : value pair
print(squares)

# Dictionary comprehension is a concise way to create a dictionary using a single line of code with logic and conditions.
# It is similar to list comprehension, but instead of values, we create key : value pairs
# SYNTAX ----> { key : value for variable in iterable}

even_squares = {x: x*x for x in range(1, 11) if x % 2 == 0}
print(even_squares)

# Using Existing Dictionaries
# example : modify values
marks = {"math" : 80, "cs" : 90, "phy" : 80}
updated = {k : v + 5 for k, v in marks.items()}
print(updated)    # items() gives tuple

print("----------------------------------------------------")

# Typecasting with Dictionary
# convert to dictionary
w = dict([("a", 1), ("b", 2)])
print(w)

#Convert dictionary to other types
x = list(w)
v = set(d)
print(x)
print(v) #Converts keys onlyyyy


#Why dicyionary is fast ?
#Dictionary uses hashing on keys, so searching and accessing is O(1) on average.
