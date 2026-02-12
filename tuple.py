# TUPLES
# An ordered, immutable and indexed collection that allow duplicate values.

t1 = (20, 40, 60)
t2 = 36, 87, 66
t3 = (10,) # It is important to use comma while initializing a tuple with one element

# t4 = (10)   This is wrong. Parenthesis alone din't create a tuple, comma does.

# Accessing elements of tuple
t = (2, 8, 16, 98, 66, 23, 98, 98)

t[0] # 2       Normal indexing starting from 0
t[-1] # 23     Negative indexing
t[1 : 3]  # (8, 16)   Slicing       tuple_name(start : end)   end excluded

print(t[4])
print(t[-2])
print(t[0 : 5])

# Immutability
#t[0] = 123  #this will give error because tuples are immutable

# Why would Python create immutable structures?
# Safety,  Faster performance,  Used when data should not change

# Methods in tuple
print(t.count(98))   #count the number of time 98 appears in the tuple t
print(t.index(8))  # returns the index of the asked element
print(t.index(98))  # Since there are multiple 98's in the tuple, it will return the first occuring index

# Only few methods in tuple ----> cuz tuple is immutable

# Nested Tuple
m = (1, 2, (23, 56, 76), 66, (4, 6))

print(m[2][1])   # First index selects inner tuple and second index selects element inside it
##           Just like lists


# DIFFERENCE BETWEEN LISTS AND TUPLE

# Features                  Lists                        Tuple

# Mutability                Mutable(can be changed)      Immutable(can not be changed)
# Syntax                    [ ]                          ( )
# Performance               Slower                       Faster
# Memory usage              More                         Less
# Methods                   Many                         Very few
# Safety                    Less safe                    More safe
# Use case                  Dynamic data                 Fixed data


# Use Lists when : Data changes frequently
#                  Adding or removing elements
#                  Example: Shopping cart, Marks list

# Use Tuples when : Data should not change
#                   Fixed records
#                   Example : coordinates, settings
