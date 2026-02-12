# Sets
# An unordered, mutable collection that stores unique elements only i.e. no suplicates allowed
# unordered means no fixed positions i.e. no indexing

# Initialization
s1 = {1, 3, 5}
s2 = set((1, 2, 3, 4, 2, 3, 5))
print(s2)  # {1, 2, 3, 4, 5}   i.e. Duplicates were automatically removed

s3 = { 1, 2, 3, 3, 5}
print(s3)     # {1, 2, 3, 5}     #order may change everytime you run the program cuz no indexing and unordered
print("----------------------------------------------------------")

# NO Indexing
# print(s3[0]) -------> ERROR

s = {12, 34, 13, 22, 99}
print(s)

# Adding Elements
s.add(40)      #for adding a single element in the set
print(s)

s.update([50, 60, 70])   #for adding multiple elements in the set
print(s)
print("------------------------------------------------")
# Removing elements from the set
s.remove(13)    #shows error if the element is not present
print(s)

s.discard(22)     # No error even if the element is missing
print(s)

s.pop()       #removes a random element, not the first one
print(s)

s1.clear()    # empties the set
print(s1)
print("-----------------------------------------------")
# Set Operations
a = {1, 2, 3}
b = {3, 4, 5, 6}

print(a | b)   # Union ( | )     Add elements from both sets

print(a & b)   #Intersection ( & )    Common elements

print(a - b)    #Difference ( - )  Elements in A but not in B
print(b - a)

print(a ^ b)    #Symmetric difference ( ^ )   Elements in either A or B, but not in both

print(3 in a)    #Membership operator
#                 Why sets are fast? 
#                     Sets uses hashing --> O(1) average time
#                     Faster than lists for searching

#----------------------------------------------------------------------------------------
print("-------------------------------------------------------")
#     Hashing
# A technique that converts data into a fixed-size number using a hash function
# That fixed-size number is called a hash value (or hash code)

# Why hashing is used ?
#     Store data efficiently
#     Search data very fast
#     Avoid duplicates (in sets)
#     Store key-value pairs (in dictionaries)

# Imagine you go to a library. 
# Instead of searching book by book, each book has a unique code number.
# That code number tells you exactly where the book is.
# -> That code number is lika a hash value

# What is Hash Function ?
# A hash function takes: input (number, string, etc.)
#                        converts it into a fixed integer
#                        same input ---> always same hash value
print(hash(10))
print(hash("python"))   # it returns an integer

# How hashing works in sets 
# when you write:  s = {10, 20, 30, 50}
# python : takes 10
#          calculates its hash value
#          stores it in a memory location based on that hash
# and when you check   10 in s
# python : calculates hash(10)
#          directly jumps to that memory location
#          checks if present
# That's why searching in set is very fast (O(1) average time)

# Why Sets don' allow duplicates ?
# when adding elements:   s.add(10)
# python : calculates hash(10)
#          check if that hash already exists
#          if yes ---> doesn't add again
# so duplicates are prevented
print("-------------------------------------------------------")
#----------------------------------------------------------------------------------------

# Frozen set
# is an immutable set
fs = frozenset([1, 2, 3])
# cannot add or remove elements
# can be used as dictionary key

# Typecasting to Set
# means converting another data types (like list, tuple, string, etc.) into a set using set() function
l = [1, 2, 2, 3, 4, 4]   
m = set(l)      # list ---> set
print(m)    # all duplicates are automatically removed

t = (10, 20, 30, 20)
u = set(t)           # tuple ---> set
print(u)

z = set("programming")      # string ---> set
print(z)      # each character becomes a set element, duplicates removed

d = {"a" : 1, "b" : 2}
e = set(d)            # dictionary ---> set
print(e)      # only keys are converted into a set

print("--------------------------------------------------------")

# Nesting in Sets
# Nesting is not allowed in sets     # nesting in normal sets -----> TypeError: unhashable type: 'set'
# BUT nesting in frozen sets is allowed
y = { frozenset({1, 2}), frozenset({3, 4})}
# y = { {1, 2}, 3}   Nope  
# y = { frozenset({1, 2}), 3}   yes
print(y)
for item in y:
    print(item)
# Why does frozenset works ?
# because : it is immutable  
#           immutable objects are hashable
#           Hashablew objects can be elements of a set

# Difference between Sets and Frozensets
# Feature                     Set                Frozenset
# Mutable                     Yes                No
# Hashable                    No                 Yes
# Can be inside set           No                 Yes
# Can be dictionary key       No                 Yes

# Real Life Applications of Sets
# Use Case                                              Example
# Remove duplicates                                     Unique roll numbers
# Find common items                                     Common subjects
# Membership testing                                    Login systems
# Mthematical operations                                Venn Diagrams