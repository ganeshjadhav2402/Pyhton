# Function in Python
# Block of Statements that perform a specific task.
# def func_name(param1, param2..): -> Function Defination
#     #some work
#     return val 

# func_name(arg1,arg2..)

"""
# function definnation
def calc_sum(a, b):
    sum = a + b
    print("Sum of a & b :",sum)
    return sum

calc_sum(5, 10)

#more line of code

calc_sum(2, 8)

#more line of code

calc_sum(12, 19)
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# function definnation
"""
def calc_sum(a, b): #prameters
    return a + b

sum = calc_sum(1, 4) #function call; arguments
print(sum)
"""

"""
def print_ganesh():
    print("Ganesh")

# print_ganesh()
output = print_ganesh()
print(output) #None
"""

"""
#average of 3 nummbers
def calc_avg(a, b ,c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(3, 3, 3)
"""

"""
print("ganesh", end="$")
print("jadhav")
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Default Parameters




""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Let's Practice
# ◑ WAF to print the length of a list. (list is the parameter)
"""
cities = ["navsari", "surat", "mumbai", "valsad", "vadodara", "dhule"]
movies = ["kgf", "marco", "salar", "kgf2", "familymen"]

def print_len(list):
    print(len(list))
    
def print_list(list):
    for item in list:
        print(item, end=" ")
    
print_list(movies)
# print()
"""

# ◑ WAF to find the factorial of n. (n is the parameter)
"""
n = 5

def calc_fect(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
    
calc_fect(6)
"""

# ◑ WAF to convert USD to INR
"""
def converter(usd_val):
    inr_val = usd_val * 85.36
    print(usd_val, "USD =", inr_val, "INR")

converter(100)    
"""

# ◑ WAF to find numbers from ODD or EVEN
"""
num = int(input("Enter a Number :"))

def type(num):
    if(num / 2 == 0):
        print("EVEN")
        return
    elif(num / 2 != 0):
        print("ODD")
type(num)
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Recursion in Python
"""
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    print("END")

show(5)
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(4))
"""

# Let's Practice
# ◑ Write a recursive function to calculate the sum of first n natural nummbers. 
"""
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(5)
print(sum)
"""

# ◑ Write a recursive function to print all elements in a list.
# Hint: use list & index as parameters.
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
    
fruits = ["mango", "apple", "banana", "litchi"]

print_list(fruits)
















