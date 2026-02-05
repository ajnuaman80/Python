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
print(student.values())