# Lists. . . 
# Collection of multiple values stored in a single variable
# kind of similar to array but not
list1 = [29, 98, 66, 28] #int
list2 = ["Winter", "Spring", "Summer"] #string
list3 = ["Winter", 19, 62.87, True] #string, int, float, boolean

# Key points: Ordered(indexing), Mutable(can change), can store different data types

# Initialization (3 methods)
a = [] #empty list
b = [2, 4, 8, 10] #with simple values

c = list((17, 19, 96)) # list() function which converts any collection into a list

print(a, "\n", b, "\n", c, sep="") #deleted extra space provided by print using sep=""

# Indexing
lis = [45, 56, 67, 78, 89, 90]
#      0   1   2   3   4   5    normal positive indexing
#     -6  -5  -4  -3  -2  -1    negative indexing
print(lis[2]) 
print(lis[-4])

# What if i try to print lis[7] ? ---> Index Error

# Slicing (making parts like pieces of a bread)
# list_name[starting_index : ending index] ending index excluded
print(lis[2 : 5]) #---> 67, 78, 89

sub_list = lis[1 : 5]
print(sub_list)  #---> 56, 67, 78, 89

# list[start : stop : step]    step is 1 by default
print(lis[ : 4])  # initial empty index i.e. 0
print(lis[ :: 2]) #start to end but the difference between indexes is 2
print(lis[ : : -1]) #since the step/difference is negative, counting starts from backwards i.e. negative indexing ---> reverse of the list
print(lis[1 : : 2])
#slicing is faster and more efficient than loops for printing elements of a list

# List Methods
q = [2, 4, 16]
q.append(128) #permanent change
print(q)
q.insert(1, 120) # inserts 120 at the index 1
print(q)

q.remove(128) #delete 128 from the list
print(q)
r = q.pop() #delete last element of the list #we can store that deleted element in a variable
print(q)
print(r)
q.clear() #delete all elements of the list
print(q)

s = [34, 67, 11, 9, 69, 56, 34]
print(s.count(34)) #returns the count of 34 in the list
# print(s.sort())
# t = s.sort()
# print(t)             these will return None becuase sort and reverse changes the list permanently i.e. all changes are done to the original list
# u = s.reverse()
# print(u)
s.sort() #sorting
print(s)
s.reverse() #reverse the list
print(s)

# List Operations
m = [1, 2]
n = [3, 4]
o = ["Hello"]
p = ["World!"]

print(m + n)  #Concatination
print(o + p)
print(o * 5) #repetition
print(n * 2)
print(2 in m) #membership operator ----> check if the given element is present in the list or not
print(12 in o)

# List Comprehension
# a short and clean way to create a new list from an existing sequence
e = []  
for f in range(1, 11):
    e.append(f * f)   #will add squares from 1 to 10 to the list e
print(e)

# SYNTAX ---> [expression for item in iterable]
g = [h * h for h in range(1, 9)]    #expression = h * h, item = h, iterable = range(1,9)
print(g)

#TrySomeQuestion ;)
state = ["stupid", "dumb", "people", "here", "in", "this", "class"] #create an uppercase string using list comprehension                                                           upper = [n.upper() for n in state]

flow = ["A", "dumb", "me"] #create a length string using List Comprehension                                                                                                                                                                                   length = [len(w) for w in flow]

# with conditions
even = [i for i in range(12) if i % 2 == 0]
print(even)

# Nesting in lists
k = [ [1, 2, 3], [4, 5, 6, 7], [8, 9] ]
#         0           1           2      k[0]--> tells which list it is
#      0  1  2    0  1  2  3    0  1     k[][2]--->gives element of the selected list
print(k[1][2])
print(k[0][1])

#Create a 3x3 matrix using nested lists
y = [
    [0, 1, 3],
    [4, 9, 5],
    [3, 7, 6]
]
print(y[0][2])
print(y[2][2])
