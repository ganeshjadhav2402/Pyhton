# List in Python
# ◑ A built-in data type that stores set of values
"""
marks = [94.5, 85, 91, 87.6, 79]
print(marks)
print("which type :",type(marks))
print("length of the list :",len(marks))
print(marks[0])
print(marks[3])
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# ◑ It can store elements of diiferent types (intger, float, string, etc.)
"""
student = ["Ganesh", 85, 22, "Navsari"]
print(student[0])
student[0] = "Prashant"
print(student)

# *Strings are inmutable
# *lists are mutable

str = "hello"
print(str[0])
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# List Slicing
# ◑ Similar to String Slicing
"""
marks = [94.5, 85, 91, 87.6, 79]
print(marks[1:4])
print(marks[-3:-1])
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# List Methods: list.append(number), list.sort(), list.sort(reverse=True), 
# list.reverse(), list.insert( idx, el), list.remove(1), list.pop( idx )

"""
list = [2, 1, 3]
print(list.append(5))
print(list.sort())
print(list)
"""

"""
list1 = ["banana", "monkey", "apple", "bear", "litchi", "tiger"]
print(list1.sort(reverse=True))
print(list1.sort())
print(list1)
"""

"""
list2 = ['g', 'a', 'n', 'e', 's', 'h', 'j', 'd', 'v']
list2.sort()
print(list2)
list2.reverse()
print(list2)
"""

"""
list3 = [2, 6, 3, 1]
# list3.insert(2, 6)
# list3.remove(2)
list3.pop(2)
print(list3)
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Tuples in Python
# ◑list is mutable
# ◑tuple is immutable
# ◑ A built-in data type that lets us create immutable sequences of values.

"""
tup = (2, 1, 3, 1)
# print(type(tup))
# print(tup[0])
# print(tup[2])
print(tup.index(2)) #returns index of first occurrences
print(tup.count(1)) #counts total occurrences
"""

"""
tup2 = ("hello", 24, 22.5)
print(type(tup2))
print(tup2)
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Let's Practice
# ◑ WAP to ask the user to enter names of their 3 favorite movies & store them inn a list
"""
movies = []
movies.append(input("enter 1st movie: "))
movies.append(input("enter 2nd movie: "))
movies.append(input("enter 3rd movie: "))

print(movies)
"""

# ◑ WAP to check if a list contains a palindrome of elements.(Hint: use copy() method) 
# [1, 2, 3, 2, 1]   [1, "abc","abc", 1]

"""
list1 = [1, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("PELINDROME")
else:
    print("NOT PELINDROME")
"""


# ◑ WAP count the number of students with the "A" grade in the following tuple.
"""
grade = ("C", "D", "A", "A", "B", "B", "A")
print("Total number of Grade A :", grade.count("A"))
"""

# store the above values in a list & sort them from "A" to "D"
grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)




