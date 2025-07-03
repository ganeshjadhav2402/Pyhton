# str1 = "This is my first String. \twe are working with python."
# print(str1)

# ◑ Basic Operations
# Concatenation
"""
str1 = "Ganesh"
len1 = len(str1)
print("Length of str1 :",len1)

str2 = "Jadhav"
len2 = len(str2)
print("Length of str2 :",len2)

final_str = str1 + " " + str2
print(final_str)
print("Total Length :",len(final_str))
"""

# String Indexing find Character

"""
str = "Ganesh jadhav"
ch = str[2]
print(ch)
"""

# Slicing: Accessing part of a string
"""
str = "Ganesh jadhav"
print(str[0:7])
print(str[7:14])
print(str[7:len(str)])

str1 = "apple"
print(str1[-5:-2])
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# String Function: str.endswith("sari."), str.capitalize(), str.replace("j", "J"), str.find(word), str.count(word)
"""
str = "hello i am Ganesh jadhav from Navsari."
print(str.endswith("sari."))
print(str.capitalize())
print(str.replace("j", "J"))
print(str.find("j"))
print(str.count("i"))
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Let's Pactrice
# WAP to input user's first name & print its length
"""
user = input("enter your name: ")
print("you name length is ", len(user))
"""

# WAP to find the occurrence of '$' in a string
"""
str = "$ is in my wallet precently 5000$"
print(str.count("$"))
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Conditional Statements
# if-elif-if(SYNTAX)
"""
age = 17

if(age >= 18):
    print("You can apply for Driving License.")
elif(age <= 18):
    print("You can not apply.")
    
print("End of code")
"""

"""
light = ""

if(light == "red"):
    print("stop") #Indentation means Proper Spacing
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("wait")
else:
    print("light is broken")

print("end of code")
"""

# Students Marks based Grade
"""
marks = int(input("enter student marks : "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"
    
print("grade of the student ->", grade)
"""

#Nesting Statment
"""
age = 81

if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#Let's Practice
# ◑ WAP to check if a number by the user is odd or even
"""
user = int(input("Enter any number :"))

if(user % 2 == 0):
    print("Number", user, "is EVEN")
else:
    print("Number", user, "is ODD")
"""

# ◑ WAP to find the gratest of 3 numbers entered by the user.
"""
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if(a >= b and  a >= c):
    print("first nummber is greatest")
elif(b >= c):
    print("second nummber is greatest")
else:
    print("third nummber is greatest")
"""

# ◑ WAP to check if a number is a multiple of 7 or not.
"""
num = int(input("enter any number: "))

if(num % 7 == 0): #check this any of number 7,5,6,2,4,12 etc.
    print(num, "is a multiple of 7")
else:
    print(num, "is not multiple")
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#Let's Build a Calculator
#Our Calculator
first = input("Enter first number :")
second = input("Enter second number :")
first = int(first)
second = int(second)
print("----press key for operator (+,-,*,/,%)")
operator = input("Enter Operator :")

if(operator == "+"):
    print(first + second)
elif(operator == "-"):
    print(first - second)
elif(operator == "*"):
    print(first * second)
elif(operator == "/"):
    print(first / second)
elif(operator == "%"):
    print(first - second)
else: 
    print("Invalid Operation")



