# Dictionary in Python
# Dictionaries are used to store data values in key:value paisa
# They are unordered, mutable(changeable) & don't allow duplicate keys
"""
info = {
    "name" : "Ganesh Jadhav",
    "subjects" : ["JAVA", "C++", "Python", "JavaScript"],
    "age" : 22,
    "marks" : 89.9,
    "isadult" : True,
}
info["name"] = "ganesh" #overwrite
info["surname"] = "jadhav"
print(info)

null_dic = {}
print(null_dic)
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

student = {
    "name" : "Prashant Patil",
    "subjects" : {
        "Web" : 95,
        "c++" : 85,
        "Java" : 80,
        "eng" : 75
    }      
}

#nested dictonary
# print(student["subjects"]["eng"])

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Dictionary Methods: Dict.keys(), Dict.values(), Dict.items(), Dict.get(), Dict.update()

"""
print(student.keys()) #returns all keys
print(list(student.keys()))
print(len(list(student.keys())))

print("Dictonary Values :",list(student.values())) #returns all values

pairs = list(student.items()) #returns all (key,val) pais as tuples
print("Dictonary Items :", pairs[0])

print(student["name"])  
print(student.get("name")) #returns the key according to value

# Update Dictonary Method 
new_dict = {"name" : "Sneha Patil","age" : 21, "city" : "Vadodra"}
student.update(new_dict)
print(student)
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Set in Python
# Set is the collection of the unordered intems.
# Each element in the Set must be unique & immutable.

"""
collection = {1, 2, 3, 2, 4, 3, "ganesh", "BCA", "BCA"}

print(collection)
print(type(collection)) #Set is unordered intems.
print(len(collection)) #in set dublicate intems not allowed
"""

"""
empty = {} #empty dictonary
empty = set() #empty set; syntax
print(empty)
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Set Methods: set.add(el), set.remove(el), set.clear(), set.pop(), set.union(set2), set.intersection(set2)
"""
collection = set()
collection.add(1) #adds an element
collection.add(2)
collection.add(3)
collection.add(4)
collection.add("ganesh")
collection.add((1, 2, 3))
# collection.add([1, 2, 3]) #unhashable type: 'list'

# collection.remove(1) #remove the elem an
# collection.clear() #empties the set
print(collection)
"""

"""
collection = {"hello", "jadhav", "webdeveloper", "ganesh", "navsari", "BCA"}

print(collection.pop()) #removes the random values
print(collection.pop())
"""

"""
set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}

print(set1.union(set2))
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Let's Practice
# Store following word meanings in a python dictionary :
    # table : “a piece of furniture”, “list of facts & figures”
    # cat : “a small animal”
"""
store = {
         "cat" : "list of facts & figures",
         "table" : ["a piece of furniture", "list of facts & figures"]
}

print("Word Dictionary: ",store)
"""

# You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students.
    # ”python”, “java”, “C++”, “python”,“javascript”,
    # “java”,“python”,“java”,“C++”,“C”
"""
subject = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}

print(len(subject),"class room for",subject,"subjects")
"""


# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.
"""
marks = {}

x = int(input("Enter maths marks :"))
marks.update({"maths" : x})

y = int(input("Enter state marks :"))
marks.update({"state" : y})

z = int(input("Enter acc marks :"))
marks.update({"acc" : z})

print("Subjects Marks :", marks)
"""

# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)
num = {9, "9.0"}
num = {
    ("float", 9.0),
    ("int", 9)
}
print(num)







